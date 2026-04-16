#!/usr/bin/env python3
"""
Sora Marketing Video Generator for GettingStoned App
Uses OpenAI's Sora 2 API to create marketing videos
"""

import os
import time
import sys
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
openai = OpenAI()

# Marketing video prompts for GettingStoned app
MARKETING_PROMPTS = {
    "hero_stress_to_calm": {
        "title": "Hero Video - Stress to Calm Transformation",
        "prompt": "A 30-year-old professional in a modern office, overwhelmed by notifications and stress, scrolling through social media on their iPhone. Their face shows tension and digital overwhelm. The camera captures their cluttered desk and multiple screens showing the chaos of modern digital life. Shot on iPhone 15 Pro, cinematic depth of field, natural lighting, vertical format 9:16.",
        "duration": "8"
    },
    
    "app_discovery": {
        "title": "App Discovery Moment",
        "prompt": "The same person receives a gentle notification on their iPhone showing 'GettingStoned - Time for mindful reflection'. They open the app to see a beautiful Buddhist interface with the GettingStoned logo prominently displayed - a stylized stone with Buddhist symbols and the app name. The logo appears in the top corner of the screen. The app interface shows white and black stones with the logo visible throughout. Their expression changes from stress to curiosity and calm. Close-up of their face showing the transition from tension to peace. Shot on iPhone 15 Pro, warm lighting, vertical format 9:16.",
        "duration": "6"
    },
    
    "mantra_practice": {
        "title": "Mantra Recognition Demo",
        "prompt": "Close-up of a person's face as they chant 'Om Mani Padme Hum' into their iPhone. The GettingStoned logo is prominently displayed on the screen. The screen shows real-time speech recognition with beautiful Tibetan script appearing. White stones materialize on screen with each successful mantra count, while the GettingStoned logo remains visible in the corner. The person's eyes are closed in deep concentration. Shot on iPhone 15 Pro, warm golden lighting, vertical format 9:16.",
        "duration": "8"
    },
    
    "prostration_detection": {
        "title": "Prostration Detection Demo",
        "prompt": "A person performing traditional Buddhist prostrations in a clean, modern space. The iPhone is positioned to capture their movements with the GettingStoned logo clearly visible on screen. CoreML detection overlays show the prostration count in real-time, with the GettingStoned logo displayed prominently. The person moves with grace and intention. Shot on iPhone 15 Pro, natural lighting, vertical format 9:16.",
        "duration": "10"
    },
    
    "karma_visualization": {
        "title": "Karma Analysis Visualization",
        "prompt": "Animated data visualization showing spiritual progress over time. The GettingStoned logo appears in the corner of the screen throughout. White and black stones floating in a 3D space, forming patterns that represent karma. Charts and graphs materialize showing enlightenment probability and spiritual growth metrics. The GettingStoned logo remains visible during all visualizations. Modern, clean aesthetic with Buddhist-inspired colors. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "8"
    },
    
    "muse_eeg_integration": {
        "title": "Muse EEG Integration",
        "prompt": "A person wearing a Muse EEG headband sitting in meditation pose. The GettingStoned app is open on their iPhone with the logo clearly visible. Brain activity is visualized as flowing energy patterns around their head. The GettingStoned app shows real-time brain state analysis with the logo prominently displayed. White stones appear automatically when the person reaches a calm state. Shot on iPhone 15 Pro, soft blue lighting, vertical format 9:16.",
        "duration": "8"
    },
    
    "urban_professional": {
        "title": "Urban Professional Testimonial",
        "prompt": "A busy executive in a high-rise office using GettingStoned during a lunch break. The GettingStoned logo is clearly visible on their iPhone screen. They find a quiet corner, open the app, and engage in a 5-minute reflection session. Their stress visibly melts away as they log white stones for virtuous actions, with the logo remaining prominent throughout. Shot on iPhone 15 Pro, natural office lighting, vertical format 9:16.",
        "duration": "8"
    },
    
    "spiritual_journey": {
        "title": "Complete Spiritual Journey",
        "prompt": "A person's complete spiritual journey with GettingStoned over several months. The GettingStoned logo appears prominently throughout the entire sequence. Quick montage showing: initial app download with logo, first meditation session with logo visible, mantra practice with logo, prostration detection with logo, karma analysis with logo, and finally a transformed, enlightened state. The progression shows clear spiritual growth with the GettingStoned logo as the constant companion. Shot on iPhone 15 Pro, various lighting conditions, vertical format 9:16.",
        "duration": "15"
    }
}

def create_marketing_video(prompt_key, output_dir="./marketing_videos"):
    """Create a marketing video using Sora 2 API"""
    
    if prompt_key not in MARKETING_PROMPTS:
        print(f"❌ Unknown prompt key: {prompt_key}")
        return None
    
    prompt_data = MARKETING_PROMPTS[prompt_key]
    
    print(f"🎬 Creating: {prompt_data['title']}")
    print(f"📝 Prompt: {prompt_data['prompt'][:100]}...")
    
    try:
        # Create video with Sora 2
        video = openai.videos.create(
            model="sora-2",
            prompt=prompt_data['prompt'],
            size="720x1280",  # Vertical format for mobile
            seconds=prompt_data['duration']
        )
        
        print(f"✅ Video generation started: {video.id}")
        return video
        
    except Exception as e:
        print(f"❌ Error creating video: {e}")
        return None

def monitor_video_progress(video_id, output_dir="./marketing_videos"):
    """Monitor video generation progress and download when ready"""
    
    print(f"⏳ Monitoring video {video_id}...")
    
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
                print(f"\n✅ Video completed: {video.id}")
                break
            elif video.status == "failed":
                error_msg = getattr(getattr(video, "error", None), "message", "Video generation failed")
                print(f"\n❌ Video failed: {error_msg}")
                return None
            
            time.sleep(2)
            
        except Exception as e:
            print(f"\n❌ Error monitoring video: {e}")
            return None
    
    # Download the video
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        content = openai.videos.download_content(video_id, variant="video")
        filename = f"{video_id}_marketing_video.mp4"
        filepath = os.path.join(output_dir, filename)
        
        content.write_to_file(filepath)
        print(f"💾 Video saved: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error downloading video: {e}")
        return None

def create_marketing_sequence():
    """Create a sequence of marketing videos"""
    
    print("🎬 GettingStoned Marketing Video Generator")
    print("=" * 50)
    
    # Create output directory
    output_dir = "./marketing_videos"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate videos
    videos = []
    
    for prompt_key in MARKETING_PROMPTS.keys():
        print(f"\n🎥 Generating: {MARKETING_PROMPTS[prompt_key]['title']}")
        
        video = create_marketing_video(prompt_key, output_dir)
        if video:
            videos.append(video)
            time.sleep(3)  # Brief pause between requests
    
    # Monitor all videos
    print(f"\n⏳ Monitoring {len(videos)} videos...")
    
    completed_videos = []
    for video in videos:
        filepath = monitor_video_progress(video.id, output_dir)
        if filepath:
            completed_videos.append(filepath)
    
    print(f"\n✅ Marketing video generation complete!")
    print(f"📁 Videos saved to: {output_dir}")
    print(f"🎬 Generated {len(completed_videos)} videos")
    
    return completed_videos

def create_single_video(prompt_key):
    """Create a single marketing video"""
    
    if prompt_key not in MARKETING_PROMPTS:
        print(f"❌ Available prompts: {list(MARKETING_PROMPTS.keys())}")
        return None
    
    print(f"🎬 Creating single video: {prompt_key}")
    
    video = create_marketing_video(prompt_key)
    if video:
        return monitor_video_progress(video.id)
    
    return None

def list_available_prompts():
    """List all available marketing video prompts"""
    
    print("📋 Available Marketing Video Prompts:")
    print("=" * 50)
    
    for key, data in MARKETING_PROMPTS.items():
        print(f"\n🎬 {key}")
        print(f"   Title: {data['title']}")
        print(f"   Duration: {data['duration']} seconds")
        print(f"   Prompt: {data['prompt'][:80]}...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            list_available_prompts()
        elif command == "single":
            if len(sys.argv) > 2:
                prompt_key = sys.argv[2]
                create_single_video(prompt_key)
            else:
                print("❌ Usage: python sora_marketing_generator.py single <prompt_key>")
                list_available_prompts()
        elif command == "all":
            create_marketing_sequence()
        else:
            print("❌ Unknown command. Use: list, single <key>, or all")
    else:
        print("🎬 GettingStoned Sora Marketing Video Generator")
        print("\nUsage:")
        print("  python sora_marketing_generator.py list                    # List all prompts")
        print("  python sora_marketing_generator.py single <prompt_key>     # Create single video")
        print("  python sora_marketing_generator.py all                     # Create all videos")
        print("\nExample:")
        print("  python sora_marketing_generator.py single hero_stress_to_calm")
