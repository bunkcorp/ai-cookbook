#!/usr/bin/env python3
"""
Sora Enhanced Videos with GettingStoned Screenshots
Uses actual app screenshots to create more accurate video prompts
"""

import os
import time
import sys
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
openai = OpenAI()

# Screenshot-based enhanced video prompts
SCREENSHOT_ENHANCED_VIDEOS = {
    "app_interface_hero": {
        "title": "App Interface Hero - Based on Real Screenshots",
        "prompt": "A person using the GettingStoned app on their iPhone, showing the actual app interface from the screenshots. The GettingStoned app icon is prominently displayed in the top corner of the iPhone screen throughout the interaction. The app displays the real interface elements as seen in the actual app screenshots. The person's face shows transformation from stress to calm as they interact with the real app interface. The GettingStoned app icon remains clearly visible throughout the video. Shot on iPhone 15 Pro, vertical format 9:16, matching the actual app design from screenshots.",
        "duration": "8"
    },
    
    "stone_logging_demo": {
        "title": "Stone Logging Demo - Real Interface",
        "prompt": "Close-up of a person using the GettingStoned app to log white and black stones. The person taps a black stone button, then selects from the 10 non-virtues list (killing, harsh speech, gossip, stealing, sexual misconduct, greed, anger, wrong view, deceit, envy). The GettingStoned app icon is prominently displayed in the top corner of the iPhone screen throughout the interaction. The app interface shows the actual stone logging process with virtue/non-virtue selection. Shot on iPhone 15 Pro, vertical format 9:16, showing the real app functionality from screenshots.",
        "duration": "8"
    },
    
    "karma_visualization_real": {
        "title": "Karma Visualization - Real App Design",
        "prompt": "A person viewing their karma visualization in the GettingStoned app, showing the actual data visualization interface from the screenshots. The app displays the real karma analysis with the GettingStoned logo prominently featured. Charts and graphs appear exactly as designed in the actual app. The GettingStoned logo remains visible throughout the visualization. Shot on iPhone 15 Pro, vertical format 9:16, matching the real app design from screenshots.",
        "duration": "8"
    },
    
    "meditation_tracking_real": {
        "title": "Meditation Tracking - Actual App Interface",
        "prompt": "A person using the GettingStoned app for meditation tracking, showing the real meditation interface from the screenshots. The app displays the actual meditation features with the GettingStoned logo clearly visible. The person's face shows deep concentration as they use the real app features. The GettingStoned logo appears exactly as designed in the actual app. Shot on iPhone 15 Pro, vertical format 9:16, using the real app interface from screenshots.",
        "duration": "8"
    },
    
    "settings_profile_real": {
        "title": "Settings & Profile - Real App Design",
        "prompt": "A person navigating the GettingStoned app settings and profile sections, showing the actual interface from the screenshots. The app displays the real settings screen with the GettingStoned logo prominently featured. The person interacts with the actual app features as designed. The GettingStoned logo remains visible throughout the settings interface. Shot on iPhone 15 Pro, vertical format 9:16, matching the real app design from screenshots.",
        "duration": "8"
    },
    
    "mantra_recognition_real": {
        "title": "Mantra Recognition - Actual App Feature",
        "prompt": "A person using the GettingStoned app for mantra recognition, showing the real speech recognition interface from the screenshots. The app displays the actual mantra tracking with the GettingStoned logo clearly visible. The person chants while the app shows real-time recognition. The GettingStoned logo appears exactly as designed in the actual app. Shot on iPhone 15 Pro, vertical format 9:16, using the real app interface from screenshots.",
        "duration": "8"
    },
    
    "prostration_detection_real": {
        "title": "Prostration Detection - Real App Interface",
        "prompt": "A person using the GettingStoned app for prostration detection, showing the actual CoreML interface from the screenshots. The app displays the real movement tracking with the GettingStoned logo prominently featured. The person performs prostrations while the app shows real-time detection. The GettingStoned logo remains visible throughout the detection interface. Shot on iPhone 15 Pro, vertical format 9:16, matching the real app design from screenshots.",
        "duration": "8"
    },
    
    "muse_eeg_integration_real": {
        "title": "Muse EEG Integration - Actual App Design",
        "prompt": "A person wearing a Muse EEG headband using the GettingStoned app, showing the real brain activity interface from the screenshots. The app displays the actual EEG integration with the GettingStoned logo clearly visible. Brain activity is visualized exactly as designed in the real app. The GettingStoned logo appears prominently throughout the EEG interface. Shot on iPhone 15 Pro, vertical format 9:16, using the real app design from screenshots.",
        "duration": "8"
    },
    
    "carplay_integration_real": {
        "title": "CarPlay Integration - Real App Design",
        "prompt": "A person using GettingStoned in their car with CarPlay integration, showing the actual CarPlay interface from the screenshots. The app displays the real driving karma tracking with the GettingStoned logo prominently featured. The person drives while the app shows real-time ethical navigation. The GettingStoned logo remains visible throughout the CarPlay interface. Shot on iPhone 15 Pro, vertical format 9:16, matching the real app design from screenshots.",
        "duration": "8"
    },
    
    "complete_user_journey_real": {
        "title": "Complete User Journey - Real App Experience",
        "prompt": "A person's complete journey using the GettingStoned app, showing all the actual interfaces from the screenshots. The app displays the real user experience with the GettingStoned logo prominently featured throughout. The person progresses through meditation, stone logging, karma analysis, and all app features as designed. The GettingStoned logo appears exactly as designed in the actual app across all interfaces. Shot on iPhone 15 Pro, vertical format 9:16, using the real app design from screenshots.",
        "duration": "8"
    }
}

def create_screenshot_enhanced_video(prompt_key, output_dir="./screenshot_enhanced_videos"):
    """Create a screenshot-enhanced video using Sora 2 API"""
    
    if prompt_key not in SCREENSHOT_ENHANCED_VIDEOS:
        print(f"❌ Unknown prompt key: {prompt_key}")
        return None
    
    prompt_data = SCREENSHOT_ENHANCED_VIDEOS[prompt_key]
    
    print(f"🎬 Creating: {prompt_data['title']}")
    print(f"📱 Screenshot-Enhanced: {prompt_data['prompt'][:100]}...")
    
    try:
        # Create video with Sora 2
        video = openai.videos.create(
            model="sora-2",
            prompt=prompt_data['prompt'],
            size="720x1280",  # Vertical format for mobile
            seconds=prompt_data['duration']
        )
        
        print(f"✅ Screenshot-enhanced video generation started: {video.id}")
        return video
        
    except Exception as e:
        print(f"❌ Error creating screenshot-enhanced video: {e}")
        return None

def monitor_screenshot_enhanced_video(video_id, output_dir="./screenshot_enhanced_videos"):
    """Monitor screenshot-enhanced video generation progress and download when ready"""
    
    print(f"⏳ Monitoring screenshot-enhanced video {video_id}...")
    
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
                print(f"\n✅ Screenshot-enhanced video completed: {video.id}")
                break
            elif video.status == "failed":
                error_msg = getattr(getattr(video, "error", None), "message", "Video generation failed")
                print(f"\n❌ Screenshot-enhanced video failed: {error_msg}")
                return None
            
            time.sleep(2)
            
        except Exception as e:
            print(f"\n❌ Error monitoring screenshot-enhanced video: {e}")
            return None
    
    # Download the video
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        content = openai.videos.download_content(video_id, variant="video")
        filename = f"{video_id}_screenshot_enhanced_video.mp4"
        filepath = os.path.join(output_dir, filename)
        
        content.write_to_file(filepath)
        print(f"💾 Screenshot-enhanced video saved: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error downloading screenshot-enhanced video: {e}")
        return None

def create_screenshot_enhanced_sequence():
    """Create a sequence of screenshot-enhanced videos"""
    
    print("🎬 GettingStoned Screenshot-Enhanced Video Generator")
    print("=" * 50)
    print("📱 Creating videos based on real app screenshots")
    print("🎯 Accurate app interface representation")
    print("=" * 50)
    
    # Create output directory
    output_dir = "./screenshot_enhanced_videos"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate screenshot-enhanced videos
    videos = []
    
    for prompt_key in SCREENSHOT_ENHANCED_VIDEOS.keys():
        print(f"\n🎥 Generating: {SCREENSHOT_ENHANCED_VIDEOS[prompt_key]['title']}")
        
        video = create_screenshot_enhanced_video(prompt_key, output_dir)
        if video:
            videos.append(video)
            time.sleep(3)  # Brief pause between requests
    
    # Monitor all videos
    print(f"\n⏳ Monitoring {len(videos)} screenshot-enhanced videos...")
    
    completed_videos = []
    for video in videos:
        filepath = monitor_screenshot_enhanced_video(video.id, output_dir)
        if filepath:
            completed_videos.append(filepath)
    
    print(f"\n✅ Screenshot-enhanced video generation complete!")
    print(f"📁 Videos saved to: {output_dir}")
    print(f"🎬 Generated {len(completed_videos)} screenshot-enhanced videos")
    print(f"📱 Each video matches your actual app design")
    
    return completed_videos

def create_single_screenshot_enhanced_video(prompt_key):
    """Create a single screenshot-enhanced video"""
    
    if prompt_key not in SCREENSHOT_ENHANCED_VIDEOS:
        print(f"❌ Available screenshot-enhanced prompts: {list(SCREENSHOT_ENHANCED_VIDEOS.keys())}")
        return None
    
    print(f"🎬 Creating screenshot-enhanced video: {prompt_key}")
    
    video = create_screenshot_enhanced_video(prompt_key)
    if video:
        return monitor_screenshot_enhanced_video(video.id)
    
    return None

def list_screenshot_enhanced_prompts():
    """List all available screenshot-enhanced video prompts"""
    
    print("📋 Available Screenshot-Enhanced Video Prompts:")
    print("=" * 50)
    
    for key, data in SCREENSHOT_ENHANCED_VIDEOS.items():
        print(f"\n🎬 {key}")
        print(f"   Title: {data['title']}")
        print(f"   Duration: {data['duration']} seconds")
        print(f"   Message: {data['prompt'][:80]}...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            list_screenshot_enhanced_prompts()
        elif command == "single":
            if len(sys.argv) > 2:
                prompt_key = sys.argv[2]
                create_single_screenshot_enhanced_video(prompt_key)
            else:
                print("❌ Usage: python sora_enhanced_with_screenshots.py single <prompt_key>")
                list_screenshot_enhanced_prompts()
        elif command == "all":
            create_screenshot_enhanced_sequence()
        else:
            print("❌ Unknown command. Use: list, single <key>, or all")
    else:
        print("🎬 GettingStoned Screenshot-Enhanced Video Generator")
        print("📱 Based on real app screenshots")
        print("\nUsage:")
        print("  python sora_enhanced_with_screenshots.py list                    # List all screenshot-enhanced prompts")
        print("  python sora_enhanced_with_screenshots.py single <prompt_key>     # Create single screenshot-enhanced video")
        print("  python sora_enhanced_with_screenshots.py all                     # Create all screenshot-enhanced videos")
        print("\nExample:")
        print("  python sora_enhanced_with_screenshots.py single app_interface_hero")
        print("\n📱 Screenshot-enhanced videos match your actual app design")
