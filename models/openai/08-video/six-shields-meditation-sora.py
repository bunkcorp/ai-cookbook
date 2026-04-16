"""
Generate a short Sora clip inspired by the "six light shields" visualization
(Green Tara practice — abstract / thangka-style, not a depiction of any real person).

Requires: OPENAI_API_KEY with Sora access, and `pip install -r requirements.txt`.

Usage:
  export OPENAI_API_KEY="sk-..."
  python six-shields-meditation-sora.py
"""

import os
import sys
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROMPT = """Cinematic CG animation inspired by Tibetan thangka painting, slow calm camera orbiting a stylized seated Green Tara figure—not a photoreal human: she looks like carved jade, gilt bronze, and painted silk with a softly idealized mask-like face and gemstone-like eyes, serene and small on screen so fine detail is suggested not literal.

From the center of her chest, brilliant white luminous mist streams outward like clouds lifting off mountain water, filling the frame with soft volumetric light. Six nested translucent egg-shaped shields form in sequence around her and a faint meditator silhouette beneath her blessing, each shell one seamless piece of living light—no cracks or panels—strong and crystalline:

first shell pure snow white pacifying light,
second warm liquid gold,
third vivid vermillion and coral red,
fourth deep starlit indigo,
fifth rich emerald green,
sixth muted bronze and mustard rust.

The shells are nested like Russian dolls but enormous, each layer slightly farther in depth, parallax as the camera drifts. Between the shells, slow spirals of translucent crystal utpala lotus petals and motes of light drift through open luminous void. Subtle anamorphic flare, gentle film grain, no text, no logos, no faces of real people, contemplative sacred mood, vertical 9:16."""

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def main() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        print(
            "OPENAI_API_KEY is not set. Export it or add it to a .env file in this folder.",
            file=sys.stderr,
        )
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = OpenAI()

    print("Submitting Sora job…")
    video = client.videos.create(
        model="sora-2",
        prompt=PROMPT,
        size="720x1280",
        seconds="8",
    )
    print("Started:", video.id, video.status)

    progress = getattr(video, "progress", 0)
    bar_length = 30
    while video.status in ("in_progress", "queued"):
        video = client.videos.retrieve(video.id)
        progress = getattr(video, "progress", 0)
        filled = int((progress / 100) * bar_length)
        bar = "=" * filled + "-" * (bar_length - filled)
        label = "Queued" if video.status == "queued" else "Processing"
        sys.stdout.write(f"\r{label}: [{bar}] {progress:.1f}%")
        sys.stdout.flush()
        time.sleep(2)
    sys.stdout.write("\n")

    if video.status == "failed":
        err = getattr(getattr(video, "error", None), "message", "Video generation failed")
        print(err, file=sys.stderr)
        sys.exit(1)

    path = os.path.join(OUTPUT_DIR, f"six-shields-meditation-{video.id}.mp4")
    print("Downloading to", path)
    content = client.videos.download_content(video.id, variant="video")
    content.write_to_file(path)
    print("Done:", path)


if __name__ == "__main__":
    main()
