"""
Long "six light shields" visualization for Sora — chains one create + several extends.

API limits (current OpenAI Python SDK / Sora):
  - create: up to 12 seconds
  - extend: each segment 4, 8, 12, 16, or 20 seconds; chain on the latest completed video

Default run: 12s base + 4×20s extends ≈ 92 seconds total (one stitched MP4 from the last job).

Requires: OPENAI_API_KEY with Sora access, repo-root or local .env (python-dotenv).

Usage:
  cd models/openai/08-video && source .venv/bin/activate
  python six-shields-meditation-sora-long.py
  python six-shields-meditation-sora-long.py --extends 4 --extend-seconds 20
"""

from __future__ import annotations

import argparse
import os
import sys
import time

import httpx
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.video import Video

load_dotenv()

STYLE = """Cinematic CG animation inspired by Tibetan thangka painting, vertical 9:16.
Stylized seated Green Tara figure—not a photoreal human: carved jade, gilt bronze, painted silk,
softly idealized mask-like face, gemstone-like eyes, serene, small on screen so detail is suggested not literal.
No text, no logos, no faces of real people, contemplative sacred mood, gentle film grain."""

BASE_PROMPT = f"""{STYLE}

Slow calm camera orbiting the figure. From her heart, brilliant white luminous mist streams outward like clouds off mountain water.
The first translucent egg-shaped shell completes around her and a faint meditator silhouette—pure snow-white pacifying light, seamless crystalline surface, no cracks.
A second shell of warm liquid gold begins forming outside it, same egg-like luminous glass, enormous nested depth and parallax."""

CONTINUE = "Seamlessly continue the exact same scene, same figure, same palette and lighting, same camera language—no jump cut, no new characters."

EXTEND_PROMPTS = [
    f"""{CONTINUE}
The golden shell locks in fully; a third vivid vermillion-and-coral shell blooms outside, cutting through inner light with controlled power.
Camera drifts through parallax layers; petals of light suggest utpala forms in the void between shells.""",
    f"""{CONTINUE}
A fourth deep starlit indigo shell wraps outward; then a fifth rich emerald shell, compassionate cool radiance.
Between shells, slow spirals of translucent crystal lotus petals and soft motes drift through open luminous space.""",
    f"""{CONTINUE}
A sixth muted bronze-and-mustard-rust shell completes the nest—all six nested egg-shields stable, transparent, impossibly strong.
The inner white and gold layers still breathe faintly; outer rust shell steadies the whole mandala of light.""",
    f"""{CONTINUE}
The camera eases back to a wider meditative framing; light softens into a calm resolving glow, petals slow to a near stillness,
contemplative closure, no sudden motion.""",
]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def poll_video(client: OpenAI, video: Video, label: str) -> Video:
    bar_length = 30
    vid = video
    print(f"{label} started:", vid.id, vid.status)
    while vid.status in ("in_progress", "queued"):
        vid = client.videos.retrieve(vid.id)
        progress = getattr(vid, "progress", 0)
        filled = int((progress / 100) * bar_length)
        bar = "=" * filled + "-" * (bar_length - filled)
        status_text = "Queued" if vid.status == "queued" else "Processing"
        sys.stdout.write(f"\r{label}: [{bar}] {progress:.1f}%")
        sys.stdout.flush()
        time.sleep(2)
    sys.stdout.write("\n")
    if vid.status == "failed":
        err = getattr(getattr(vid, "error", None), "message", "Video generation failed")
        print(err, file=sys.stderr)
        sys.exit(1)
    return vid


def download_mp4(client: OpenAI, video_id: str, dest: str) -> None:
    client.videos.download_content(video_id, variant="video").write_to_file(dest)


def submit_extend_json(
    *,
    extensions_url: str,
    api_key: str,
    source_video_id: str,
    prompt: str,
    seconds: str,
) -> str:
    """
    POST .../videos/extensions with JSON body.
    The Python SDK's videos.extend() uses multipart; this API expects JSON (video id reference).
    """
    r = httpx.post(
        extensions_url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "video": {"id": source_video_id},
            "prompt": prompt,
            "seconds": seconds,
        },
        timeout=httpx.Timeout(600.0, connect=30.0),
    )
    if r.is_error:
        try:
            detail = r.json()
        except Exception:
            detail = r.text
        raise RuntimeError(f"Extend request failed ({r.status_code}): {detail}") from None
    body = r.json()
    return body["id"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Long six-shields Sora video via create + extend chain.")
    parser.add_argument(
        "--extends",
        type=int,
        default=4,
        metavar="N",
        help="Number of extend segments after the 12s base (default 4 → ~92s total with 20s extends).",
    )
    parser.add_argument(
        "--extend-seconds",
        choices=("4", "8", "12", "16", "20"),
        default="20",
        help="Duration of each extend segment (default 20).",
    )
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        print(
            "OPENAI_API_KEY is not set. Export it or use a .env at repo root / this folder.",
            file=sys.stderr,
        )
        sys.exit(1)

    n_ext = args.extends
    if n_ext < 0:
        print("--extends must be >= 0", file=sys.stderr)
        sys.exit(1)
    if n_ext > len(EXTEND_PROMPTS):
        print(
            f"--extends max is {len(EXTEND_PROMPTS)} (add more EXTEND_PROMPTS entries to go longer).",
            file=sys.stderr,
        )
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = OpenAI()
    api_key = os.environ["OPENAI_API_KEY"]
    extensions_url = str(client.base_url).rstrip("/") + "/videos/extensions"

    print("Submitting base Sora job (12s)…")
    video = client.videos.create(
        model="sora-2",
        prompt=BASE_PROMPT,
        size="720x1280",
        seconds="12",
    )
    video = poll_video(client, video, "Base")
    current_id = video.id

    for i in range(n_ext):
        prompt = EXTEND_PROMPTS[i]
        print(f"\nSubmitting extend {i + 1}/{n_ext} ({args.extend_seconds}s)…")
        ext_id = submit_extend_json(
            extensions_url=extensions_url,
            api_key=api_key,
            source_video_id=current_id,
            prompt=prompt,
            seconds=args.extend_seconds,
        )
        video = client.videos.retrieve(ext_id)
        video = poll_video(client, video, f"Extend {i + 1}")
        current_id = video.id

    path = os.path.join(OUTPUT_DIR, f"six-shields-long-{video.id}.mp4")
    print("\nDownloading final stitched video to", path)
    download_mp4(client, video.id, path)
    print("Done:", path)
    print(f"Approx. length: 12s + {n_ext}×{args.extend_seconds}s (stitched by API).")


if __name__ == "__main__":
    main()
