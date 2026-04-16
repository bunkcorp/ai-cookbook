#!/usr/bin/env python3
"""
Sora Marketing Videos with Call-to-Action for GettingStoned App
Enhanced prompts with clear CTAs for app downloads and engagement
"""

import os
import time
import sys
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
openai = OpenAI()

# Marketing video prompts with Call-to-Action
MARKETING_WITH_CTA = {
    "hero_stress_to_calm_cta": {
        "title": "Hero Video - Stress to Calm with CTA",
        "prompt": "A 30-year-old professional in a modern office, overwhelmed by notifications and stress, scrolling through social media on their iPhone. Their face shows tension and digital overwhelm. The camera captures their cluttered desk and multiple screens showing the chaos of modern digital life. They discover GettingStoned app and download it. Text overlay appears: 'Download GettingStoned - Transform stress into awareness' with app store button. The GettingStoned logo is prominently displayed. Shot on iPhone 15 Pro, cinematic depth of field, natural lighting, vertical format 9:16.",
        "duration": "10"
    },
    
    "app_discovery_cta": {
        "title": "App Discovery with Download CTA",
        "prompt": "The same person receives a gentle notification on their iPhone showing 'GettingStoned - Time for mindful reflection'. They open the app to see a beautiful Buddhist interface with the GettingStoned logo prominently displayed. The app interface shows white and black stones with the logo visible throughout. Their expression changes from stress to curiosity and calm. Text overlay: 'Get GettingStoned - Available on App Store' with download button. The GettingStoned logo remains visible throughout. Shot on iPhone 15 Pro, warm lighting, vertical format 9:16.",
        "duration": "8"
    },
    
    "mantra_practice_cta": {
        "title": "Mantra Recognition with CTA",
        "prompt": "Close-up of a person's face as they chant 'Om Mani Padme Hum' into their iPhone. The GettingStoned logo is prominently displayed on the screen. The screen shows real-time speech recognition with beautiful Tibetan script appearing. White stones materialize on screen with each successful mantra count. Text overlay: 'Start your spiritual journey - Download GettingStoned' with app store icon. The GettingStoned logo remains visible throughout. Shot on iPhone 15 Pro, warm golden lighting, vertical format 9:16.",
        "duration": "10"
    },
    
    "prostration_detection_cta": {
        "title": "Prostration Detection with CTA",
        "prompt": "A person performing traditional Buddhist prostrations in a clean, modern space. The iPhone shows the GettingStoned app with logo clearly visible. CoreML detection overlays show the prostration count in real-time. Text overlay: 'Track your practice - Get GettingStoned now' with download button. The GettingStoned logo is prominently displayed throughout. Shot on iPhone 15 Pro, natural lighting, vertical format 9:16.",
        "duration": "12"
    },
    
    "karma_visualization_cta": {
        "title": "Karma Analysis with CTA",
        "prompt": "Animated data visualization showing spiritual progress over time. The GettingStoned logo appears prominently. White and black stones floating in 3D space, forming patterns that represent karma. Charts and graphs materialize showing enlightenment probability. Text overlay: 'See your spiritual growth - Download GettingStoned' with app store button. The GettingStoned logo remains visible during all visualizations. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "10"
    },
    
    "muse_eeg_integration_cta": {
        "title": "Muse EEG Integration with CTA",
        "prompt": "A person wearing a Muse EEG headband sitting in meditation pose. The GettingStoned app is open with the logo clearly visible. Brain activity is visualized as flowing energy patterns. The app shows real-time brain state analysis. Text overlay: 'Connect your mind - Get GettingStoned today' with download button. White stones appear automatically when the person reaches a calm state. The GettingStoned logo remains prominent. Shot on iPhone 15 Pro, soft blue lighting, vertical format 9:16.",
        "duration": "12"
    },
    
    "urban_professional_cta": {
        "title": "Professional Testimonial with CTA",
        "prompt": "A successful urban professional in a modern office, speaking directly to camera: 'GettingStoned changed how I approach my daily challenges.' The GettingStoned logo appears prominently on their phone screen. They show the app interface with white and black stones. Text overlay: 'Join thousands finding peace - Download GettingStoned' with app store icon. The GettingStoned logo remains visible throughout. Shot on iPhone 15 Pro, professional lighting, vertical format 9:16.",
        "duration": "10"
    },
    
    "spiritual_journey_cta": {
        "title": "Complete Spiritual Journey with CTA",
        "prompt": "A person's complete spiritual journey from chaos to enlightenment using GettingStoned. The app interface shows their progression with the logo prominently displayed. White and black stones accumulate over time, showing their growth. Text overlay: 'Begin your transformation - Download GettingStoned now' with download button. The GettingStoned logo remains visible throughout their journey. Shot on iPhone 15 Pro, warm lighting, vertical format 9:16.",
        "duration": "15"
    },
    
    "manifesto_hero_cta": {
        "title": "Manifesto Hero with CTA",
        "prompt": "A person in a modern office, overwhelmed by digital chaos and stress, scrolling through endless notifications. The GettingStoned logo appears on their iPhone screen. They open the app and see the message 'Not tracking your brain — rediscovering your mind.' Text overlay: 'Beyond neuroscience — into awakening. Download GettingStoned' with app store button. The GettingStoned logo is prominently displayed. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "causal_navigation_cta": {
        "title": "Causal Navigation with CTA",
        "prompt": "A person driving with GettingStoned CarPlay integration on their dashboard. The screen shows a navigation map with glowing white and black stone zones. The GettingStoned logo is prominently displayed on the CarPlay interface. Text overlay: 'The world's first moral GPS - Get GettingStoned' with download button. The person chooses routes based on ethical clarity. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "15"
    }
}

def create_cta_video(prompt_key, output_dir="./marketing_videos_with_cta"):
    """Create a marketing video with call-to-action using Sora 2 API"""
    
    if prompt_key not in MARKETING_WITH_CTA:
        print(f"❌ Unknown prompt key: {prompt_key}")
        return None
    
    prompt_data = MARKETING_WITH_CTA[prompt_key]
    
    print(f"🎬 Creating: {prompt_data['title']}")
    print(f"📝 CTA Message: {prompt_data['prompt'][:100]}...")
    
    try:
        # Create video with Sora 2
        video = openai.videos.create(
            model="sora-2",
            prompt=prompt_data['prompt'],
            size="720x1280",  # Vertical format for mobile
            seconds=prompt_data['duration']
        )
        
        print(f"✅ CTA video generation started: {video.id}")
        return video
        
    except Exception as e:
        print(f"❌ Error creating CTA video: {e}")
        return None

def monitor_cta_video(video_id, output_dir="./marketing_videos_with_cta"):
    """Monitor CTA video generation progress and download when ready"""
    
    print(f"⏳ Monitoring CTA video {video_id}...")
    
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
                print(f"\n✅ CTA video completed: {video.id}")
                break
            elif video.status == "failed":
                error_msg = getattr(getattr(video, "error", None), "message", "Video generation failed")
                print(f"\n❌ CTA video failed: {error_msg}")
                return None
            
            time.sleep(2)
            
        except Exception as e:
            print(f"\n❌ Error monitoring CTA video: {e}")
            return None
    
    # Download the video
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        content = openai.videos.download_content(video_id, variant="video")
        filename = f"{video_id}_cta_video.mp4"
        filepath = os.path.join(output_dir, filename)
        
        content.write_to_file(filepath)
        print(f"💾 CTA video saved: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error downloading CTA video: {e}")
        return None

def create_cta_sequence():
    """Create a sequence of CTA-enhanced marketing videos"""
    
    print("🎬 GettingStoned CTA Video Generator")
    print("=" * 50)
    print("📱 Creating videos with clear calls to action")
    print("⬇️ Download prompts and app store buttons")
    print("=" * 50)
    
    # Create output directory
    output_dir = "./marketing_videos_with_cta"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate CTA videos
    videos = []
    
    for prompt_key in MARKETING_WITH_CTA.keys():
        print(f"\n🎥 Generating: {MARKETING_WITH_CTA[prompt_key]['title']}")
        
        video = create_cta_video(prompt_key, output_dir)
        if video:
            videos.append(video)
            time.sleep(3)  # Brief pause between requests
    
    # Monitor all videos
    print(f"\n⏳ Monitoring {len(videos)} CTA videos...")
    
    completed_videos = []
    for video in videos:
        filepath = monitor_cta_video(video.id, output_dir)
        if filepath:
            completed_videos.append(filepath)
    
    print(f"\n✅ CTA video generation complete!")
    print(f"📁 Videos saved to: {output_dir}")
    print(f"🎬 Generated {len(completed_videos)} CTA videos")
    print(f"📱 Each video includes clear download prompts")
    
    return completed_videos

def create_single_cta_video(prompt_key):
    """Create a single CTA video"""
    
    if prompt_key not in MARKETING_WITH_CTA:
        print(f"❌ Available CTA prompts: {list(MARKETING_WITH_CTA.keys())}")
        return None
    
    print(f"🎬 Creating CTA video: {prompt_key}")
    
    video = create_cta_video(prompt_key)
    if video:
        return monitor_cta_video(video.id)
    
    return None

def list_cta_prompts():
    """List all available CTA video prompts"""
    
    print("📋 Available CTA Video Prompts:")
    print("=" * 50)
    
    for key, data in MARKETING_WITH_CTA.items():
        print(f"\n🎬 {key}")
        print(f"   Title: {data['title']}")
        print(f"   Duration: {data['duration']} seconds")
        print(f"   CTA: {data['prompt'][:80]}...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            list_cta_prompts()
        elif command == "single":
            if len(sys.argv) > 2:
                prompt_key = sys.argv[2]
                create_single_cta_video(prompt_key)
            else:
                print("❌ Usage: python sora_marketing_with_cta.py single <prompt_key>")
                list_cta_prompts()
        elif command == "all":
            create_cta_sequence()
        else:
            print("❌ Unknown command. Use: list, single <key>, or all")
    else:
        print("🎬 GettingStoned CTA Video Generator")
        print("📱 Clear calls to action for app downloads")
        print("\nUsage:")
        print("  python sora_marketing_with_cta.py list                    # List all CTA prompts")
        print("  python sora_marketing_with_cta.py single <prompt_key>     # Create single CTA video")
        print("  python sora_marketing_with_cta.py all                     # Create all CTA videos")
        print("\nExample:")
        print("  python sora_marketing_with_cta.py single hero_stress_to_calm_cta")
        print("\n📱 CTA videos include download prompts and app store buttons")
