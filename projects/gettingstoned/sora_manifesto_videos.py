#!/usr/bin/env python3
"""
Sora Manifesto Marketing Videos for GettingStoned App
Incorporates the deep philosophy and manifesto into video generation
"""

import os
import time
import sys
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
openai = OpenAI()

# Manifesto-Enhanced Marketing Video Prompts
MANIFESTO_VIDEOS = {
    "manifesto_hero": {
        "title": "Manifesto Hero - The Modern Mirror of Mind",
        "prompt": "A person in a modern office, overwhelmed by digital chaos and stress, scrolling through endless notifications. The GettingStoned logo appears on their iPhone screen. They open the app and see the message 'Not tracking your brain — rediscovering your mind.' Their expression transforms from digital overwhelm to deep contemplation. The camera shows their face reflecting in the phone screen, symbolizing the modern mirror of mind. Shot on iPhone 15 Pro, cinematic depth of field, natural lighting, vertical format 9:16.",
        "duration": "12"
    },
    
    "karma_vs_neuroscience": {
        "title": "Karma vs Neuroscience - Beyond Brain Scans",
        "prompt": "Split screen showing a traditional EEG brain scan on one side and the GettingStoned karma visualization on the other. The EEG shows brain activity patterns, while the karma map shows ethical trajectory and spiritual growth. Text overlay appears: 'Science maps neurons — karma shows causality.' The GettingStoned logo is prominently displayed. The person chooses the karma path, symbolizing the choice between tracking brain activity and understanding spiritual causality. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "10"
    },
    
    "transformation_not_calm": {
        "title": "Transformation Not Calm - Beyond Symptom Relief",
        "prompt": "A person using a generic meditation app, looking frustrated as it only offers 'calm' and 'relaxation' features. They switch to GettingStoned and see the message 'They sell calm — you offer transformation.' The app interface shows karma analysis, ethical reflection, and spiritual growth metrics. The GettingStoned logo is clearly visible. The person's face shows understanding and purpose rather than just temporary relief. Shot on iPhone 15 Pro, warm lighting, vertical format 9:16.",
        "duration": "10"
    },
    
    "living_experiment": {
        "title": "Living Experiment in Consciousness",
        "prompt": "A person in a peaceful meditation space, using GettingStoned not as a tool but as a mirror. The app shows 'A living experiment in consciousness' on screen. The person logs white and black stones, each representing a choice in their spiritual development. The GettingStoned logo remains visible throughout. The camera captures the person's genuine engagement with their own ethical development, not just app usage. Shot on iPhone 15 Pro, soft natural lighting, vertical format 9:16.",
        "duration": "12"
    },
    
    "ancient_wisdom_modern_tech": {
        "title": "Ancient Wisdom Meets Modern Technology",
        "prompt": "Transition from ancient Tibetan monastery with monks counting stones to modern person using GettingStoned on iPhone. The GettingStoned logo bridges the gap between tradition and innovation. Text overlay: 'In the old days, monks counted stones. Now, our phones do — but the wisdom is the same.' The person's practice shows the same intention and awareness as the ancient monks, just enhanced with modern technology. Shot on iPhone 15 Pro, warm lighting, vertical format 9:16.",
        "duration": "15"
    },
    
    "beyond_neuroscience": {
        "title": "Beyond Neuroscience - Into Awakening",
        "prompt": "A person wearing a Muse EEG headband, looking at brain activity data, then switching to GettingStoned's karma analysis. The GettingStoned logo appears prominently. Text overlay: 'Science can map neurons — not nirvana. The EEG can't measure compassion. The fMRI can't record emptiness.' The person chooses the karma path, symbolizing the choice between scientific measurement and spiritual understanding. Shot on iPhone 15 Pro, soft blue lighting, vertical format 9:16.",
        "duration": "12"
    },
    
    "ethical_visibility": {
        "title": "Making Ethics Visible - The Forgotten Pillar",
        "prompt": "A person using various meditation apps that only track time and streaks, looking frustrated. They switch to GettingStoned and see the message 'They ignore ethics — you make it visible.' The app interface shows virtue tracking, ethical reflection, and moral development. The GettingStoned logo is clearly displayed. The person's face shows recognition of something deeper than just mindfulness — they see the integration of ethics and awareness. Shot on iPhone 15 Pro, natural lighting, vertical format 9:16.",
        "duration": "10"
    },
    
    "freedom_not_dependency": {
        "title": "Freedom Not Dependency - Ending the Need for Apps",
        "prompt": "A person using GettingStoned over time, showing their progression from app dependency to genuine spiritual independence. The GettingStoned logo appears throughout their journey. Text overlay: 'You're not building user dependency; you're building awareness that ends the need for apps altogether.' The person gradually uses the app less as they develop genuine spiritual awareness. The final shot shows them meditating without any device, having internalized the practice. Shot on iPhone 15 Pro, various lighting conditions, vertical format 9:16.",
        "duration": "15"
    },
    
    "modernization_not_monetization": {
        "title": "Modernization Not Monetization",
        "prompt": "A person discovering GettingStoned among other meditation apps that focus on subscriptions, premium features, and monetization. The GettingStoned logo stands out as different. Text overlay: 'GettingStoned is a modernization, not a monetization. A return to ethics, cause and effect, and the living experiment of awareness.' The person chooses GettingStoned because it offers genuine spiritual development rather than just another subscription service. Shot on iPhone 15 Pro, natural lighting, vertical format 9:16.",
        "duration": "10"
    },
    
    "who_you_really_are": {
        "title": "Who You Really Are - Action by Action",
        "prompt": "A person using GettingStoned for deep self-reflection, logging white and black stones for their daily actions. The GettingStoned logo is prominently displayed. Text overlay: 'It's showing you who you really are — action by action, thought by thought.' The person's face shows genuine self-awareness and growth as they track their ethical development. The app becomes a mirror for their spiritual journey. Shot on iPhone 15 Pro, warm lighting, vertical format 9:16.",
        "duration": "12"
    }
}

def create_manifesto_video(prompt_key, output_dir="./manifesto_videos"):
    """Create a manifesto-enhanced marketing video using Sora 2 API"""
    
    if prompt_key not in MANIFESTO_VIDEOS:
        print(f"❌ Unknown prompt key: {prompt_key}")
        return None
    
    prompt_data = MANIFESTO_VIDEOS[prompt_key]
    
    print(f"🎬 Creating: {prompt_data['title']}")
    print(f"📝 Manifesto Message: {prompt_data['prompt'][:100]}...")
    
    try:
        # Create video with Sora 2
        video = openai.videos.create(
            model="sora-2",
            prompt=prompt_data['prompt'],
            size="720x1280",  # Vertical format for mobile
            seconds=prompt_data['duration']
        )
        
        print(f"✅ Manifesto video generation started: {video.id}")
        return video
        
    except Exception as e:
        print(f"❌ Error creating manifesto video: {e}")
        return None

def monitor_manifesto_video(video_id, output_dir="./manifesto_videos"):
    """Monitor manifesto video generation progress and download when ready"""
    
    print(f"⏳ Monitoring manifesto video {video_id}...")
    
    while True:
        try:
            video = openai.videos.retrieve(video_id)
            progress = getattr(video, "progress", 0)
            
            # Progress bar
            bar_length = 30
            filled_length = int((progress / 100) * bar_length)
            bar = "=" * filled_length + "-" * (bar_length - filled_length)
            
            status_text = "Queued" if video.status == "queued" else "Processing"
            print(f"\r{status_text}: [{bar}] {progress:.1f}%", end="", flush=True)
            
            if video.status == "completed":
                print(f"\n✅ Manifesto video completed: {video.id}")
                break
            elif video.status == "failed":
                error_msg = getattr(getattr(video, "error", None), "message", "Video generation failed")
                print(f"\n❌ Manifesto video failed: {error_msg}")
                return None
            
            time.sleep(2)
            
        except Exception as e:
            print(f"\n❌ Error monitoring manifesto video: {e}")
            return None
    
    # Download the video
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        content = openai.videos.download_content(video_id, variant="video")
        filename = f"{video_id}_manifesto_video.mp4"
        filepath = os.path.join(output_dir, filename)
        
        content.write_to_file(filepath)
        print(f"💾 Manifesto video saved: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error downloading manifesto video: {e}")
        return None

def create_manifesto_sequence():
    """Create a sequence of manifesto-enhanced marketing videos"""
    
    print("🎬 GettingStoned Manifesto Video Generator")
    print("=" * 50)
    print("🪨 Creating videos that reveal the deeper purpose of GettingStoned")
    print("🧠 Beyond neuroscience — into awakening")
    print("=" * 50)
    
    # Create output directory
    output_dir = "./manifesto_videos"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate manifesto videos
    videos = []
    
    for prompt_key in MANIFESTO_VIDEOS.keys():
        print(f"\n🎥 Generating: {MANIFESTO_VIDEOS[prompt_key]['title']}")
        
        video = create_manifesto_video(prompt_key, output_dir)
        if video:
            videos.append(video)
            time.sleep(3)  # Brief pause between requests
    
    # Monitor all videos
    print(f"\n⏳ Monitoring {len(videos)} manifesto videos...")
    
    completed_videos = []
    for video in videos:
        filepath = monitor_manifesto_video(video.id, output_dir)
        if filepath:
            completed_videos.append(filepath)
    
    print(f"\n✅ Manifesto video generation complete!")
    print(f"📁 Videos saved to: {output_dir}")
    print(f"🎬 Generated {len(completed_videos)} manifesto videos")
    print(f"🪨 Each video embodies the GettingStoned philosophy")
    
    return completed_videos

def create_single_manifesto_video(prompt_key):
    """Create a single manifesto video"""
    
    if prompt_key not in MANIFESTO_VIDEOS:
        print(f"❌ Available manifesto prompts: {list(MANIFESTO_VIDEOS.keys())}")
        return None
    
    print(f"🎬 Creating manifesto video: {prompt_key}")
    
    video = create_manifesto_video(prompt_key)
    if video:
        return monitor_manifesto_video(video.id)
    
    return None

def list_manifesto_prompts():
    """List all available manifesto video prompts"""
    
    print("📋 Available Manifesto Video Prompts:")
    print("=" * 50)
    
    for key, data in MANIFESTO_VIDEOS.items():
        print(f"\n🎬 {key}")
        print(f"   Title: {data['title']}")
        print(f"   Duration: {data['duration']} seconds")
        print(f"   Message: {data['prompt'][:80]}...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            list_manifesto_prompts()
        elif command == "single":
            if len(sys.argv) > 2:
                prompt_key = sys.argv[2]
                create_single_manifesto_video(prompt_key)
            else:
                print("❌ Usage: python sora_manifesto_videos.py single <prompt_key>")
                list_manifesto_prompts()
        elif command == "all":
            create_manifesto_sequence()
        else:
            print("❌ Unknown command. Use: list, single <key>, or all")
    else:
        print("🎬 GettingStoned Manifesto Video Generator")
        print("🪨 Beyond neuroscience — into awakening")
        print("\nUsage:")
        print("  python sora_manifesto_videos.py list                    # List all manifesto prompts")
        print("  python sora_manifesto_videos.py single <prompt_key>     # Create single manifesto video")
        print("  python sora_manifesto_videos.py all                     # Create all manifesto videos")
        print("\nExample:")
        print("  python sora_manifesto_videos.py single manifesto_hero")
        print("\n🪨 Manifesto videos reveal the deeper purpose of GettingStoned")
