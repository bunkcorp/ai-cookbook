#!/usr/bin/env python3
"""
Sora Enhanced Ecosystem Videos for GettingStoned App
Incorporates CarPlay integration, ethical navigation, and global karma mapping
"""

import os
import time
import sys
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
openai = OpenAI()

# Enhanced Ecosystem Video Prompts
ECOSYSTEM_VIDEOS = {
    "causal_navigation_system": {
        "title": "Causal Navigation System - The World's First Moral GPS",
        "prompt": "A person driving with GettingStoned CarPlay integration on their dashboard. The screen shows a navigation map with glowing white and black stone zones, representing ethical density of different areas. The person chooses routes based on ethical clarity, avoiding black-stone clusters and seeking white-stone zones. The GettingStoned logo is prominently displayed on the CarPlay interface. Text overlay: 'The world's first causal navigation system.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "15"
    },
    
    "karmic_co_pilot": {
        "title": "Karmic Co-Pilot - Ethical Driving Assistant",
        "prompt": "A person driving calmly and attentively with GettingStoned CarPlay integration. The dashboard shows their driving karma index in real-time, with white stones appearing for patient yielding and smooth acceleration. The GettingStoned logo is clearly visible on the CarPlay screen. The person's driving reflects mindfulness and compassion. Text overlay: 'When you drive with care, the world brightens.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "global_karma_atlas": {
        "title": "Global Karma Atlas - Ethical Reputation Everywhere",
        "prompt": "A world map glowing with white and black stone zones, representing collective virtue and misconduct across the globe. The GettingStoned logo appears prominently. Businesses and locations glow with their true ethical nature, not fake reviews. The map shows areas of kindness, safety, and respect versus areas of aggression and harm. Text overlay: 'Reputation becomes transparent. Awareness becomes visible.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "15"
    },
    
    "moral_gps_navigation": {
        "title": "Moral GPS Navigation - Choose Routes Based on Ethics",
        "prompt": "A person using GettingStoned navigation to choose routes based on ethical clarity. The map shows white-stone zones of kindness and black-stone clusters of negativity. The person navigates away from harmful areas and toward virtuous ones. The GettingStoned logo is prominently displayed. Text overlay: 'Navigate away from negativity, choose routes that radiate ethical clarity.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "reputation_revolution": {
        "title": "Reputation Revolution - Truth from Traceable Intention",
        "prompt": "A person looking at a business on GettingStoned's karma map, seeing its true ethical nature through white-stone density rather than fake online reviews. The GettingStoned logo is clearly visible. The business glows with genuine virtue, showing redemption and recovery from past harm. Text overlay: 'Unlike review platforms that amplify outrage, GettingStoned builds truth from traceable intention.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "10"
    },
    
    "ethical_geolocation": {
        "title": "Ethical Geolocation - Moral Audit Trail",
        "prompt": "A person using GettingStoned to see the ethical density of their surroundings. The app shows white-stone zones of kindness and black-stone clusters of misconduct. The person chooses to visit places that radiate ethical clarity. The GettingStoned logo is prominently displayed. Text overlay: 'It's a moral audit trail, not a comment war.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "10"
    },
    
    "living_karma_map": {
        "title": "Living Karma Map - Real-Time Ethical Patterns",
        "prompt": "A dynamic visualization of global ethical patterns in real-time. White and black stones flow across the map, showing how collective virtue and misconduct spread and evolve. The GettingStoned logo appears prominently. The map reveals the interconnected nature of all actions and their consequences. Text overlay: 'Each choice becomes part of the world's living karma map.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "15"
    },
    
    "beyond_apps_ecosystem": {
        "title": "Beyond Apps - Complete Spiritual Ecosystem",
        "prompt": "A person using GettingStoned across multiple contexts: meditation at home, driving with CarPlay, navigating with ethical GPS, and checking business karma. The GettingStoned logo appears consistently across all interfaces. The person's spiritual development is tracked through their daily choices and actions. Text overlay: 'You don't escape the system — you awaken within it.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "18"
    },
    
    "causal_navigation_manifesto": {
        "title": "Causal Navigation Manifesto - Beyond Metrics, Toward Meaning",
        "prompt": "A person using GettingStoned's complete ecosystem, from meditation to driving to navigation. The GettingStoned logo appears prominently throughout. Text overlay: 'GettingStoned — the world's first causal navigation system. Beyond metrics, toward meaning. The modern mirror of mind.' The person's journey shows transformation from individual practice to global ethical awareness. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "20"
    },
    
    "monks_to_cars": {
        "title": "Monks to Cars - Ancient Wisdom, Modern Technology",
        "prompt": "Transition from ancient Tibetan monastery with monks counting stones to modern person using GettingStoned in their car with CarPlay integration. The GettingStoned logo bridges the gap between tradition and innovation. Text overlay: 'In the old days, monks counted stones. Now, our cars and phones do. The wisdom is timeless. The reflection is real.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "15"
    }
}

def create_ecosystem_video(prompt_key, output_dir="./ecosystem_videos"):
    """Create an ecosystem-enhanced marketing video using Sora 2 API"""
    
    if prompt_key not in ECOSYSTEM_VIDEOS:
        print(f"❌ Unknown prompt key: {prompt_key}")
        return None
    
    prompt_data = ECOSYSTEM_VIDEOS[prompt_key]
    
    print(f"🎬 Creating: {prompt_data['title']}")
    print(f"📝 Ecosystem Message: {prompt_data['prompt'][:100]}...")
    
    try:
        # Create video with Sora 2
        video = openai.videos.create(
            model="sora-2",
            prompt=prompt_data['prompt'],
            size="720x1280",  # Vertical format for mobile
            seconds=prompt_data['duration']
        )
        
        print(f"✅ Ecosystem video generation started: {video.id}")
        return video
        
    except Exception as e:
        print(f"❌ Error creating ecosystem video: {e}")
        return None

def monitor_ecosystem_video(video_id, output_dir="./ecosystem_videos"):
    """Monitor ecosystem video generation progress and download when ready"""
    
    print(f"⏳ Monitoring ecosystem video {video_id}...")
    
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
                print(f"\n✅ Ecosystem video completed: {video.id}")
                break
            elif video.status == "failed":
                error_msg = getattr(getattr(video, "error", None), "message", "Video generation failed")
                print(f"\n❌ Ecosystem video failed: {error_msg}")
                return None
            
            time.sleep(2)
            
        except Exception as e:
            print(f"\n❌ Error monitoring ecosystem video: {e}")
            return None
    
    # Download the video
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        content = openai.videos.download_content(video_id, variant="video")
        filename = f"{video_id}_ecosystem_video.mp4"
        filepath = os.path.join(output_dir, filename)
        
        content.write_to_file(filepath)
        print(f"💾 Ecosystem video saved: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error downloading ecosystem video: {e}")
        return None

def create_ecosystem_sequence():
    """Create a sequence of ecosystem-enhanced marketing videos"""
    
    print("🎬 GettingStoned Ecosystem Video Generator")
    print("=" * 50)
    print("🚗 Creating videos for the world's first causal navigation system")
    print("🗺️ From meditation to driving to global karma mapping")
    print("=" * 50)
    
    # Create output directory
    output_dir = "./ecosystem_videos"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate ecosystem videos
    videos = []
    
    for prompt_key in ECOSYSTEM_VIDEOS.keys():
        print(f"\n🎥 Generating: {ECOSYSTEM_VIDEOS[prompt_key]['title']")
        
        video = create_ecosystem_video(prompt_key, output_dir)
        if video:
            videos.append(video)
            time.sleep(3)  # Brief pause between requests
    
    # Monitor all videos
    print(f"\n⏳ Monitoring {len(videos)} ecosystem videos...")
    
    completed_videos = []
    for video in videos:
        filepath = monitor_ecosystem_video(video.id, output_dir)
        if filepath:
            completed_videos.append(filepath)
    
    print(f"\n✅ Ecosystem video generation complete!")
    print(f"📁 Videos saved to: {output_dir}")
    print(f"🎬 Generated {len(completed_videos)} ecosystem videos")
    print(f"🚗 Each video showcases the complete GettingStoned ecosystem")
    
    return completed_videos

def create_single_ecosystem_video(prompt_key):
    """Create a single ecosystem video"""
    
    if prompt_key not in ECOSYSTEM_VIDEOS:
        print(f"❌ Available ecosystem prompts: {list(ECOSYSTEM_VIDEOS.keys())}")
        return None
    
    print(f"🎬 Creating ecosystem video: {prompt_key}")
    
    video = create_ecosystem_video(prompt_key)
    if video:
        return monitor_ecosystem_video(video.id)
    
    return None

def list_ecosystem_prompts():
    """List all available ecosystem video prompts"""
    
    print("📋 Available Ecosystem Video Prompts:")
    print("=" * 50)
    
    for key, data in ECOSYSTEM_VIDEOS.items():
        print(f"\n🎬 {key}")
        print(f"   Title: {data['title']}")
        print(f"   Duration: {data['duration']} seconds")
        print(f"   Message: {data['prompt'][:80]}...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            list_ecosystem_prompts()
        elif command == "single":
            if len(sys.argv) > 2:
                prompt_key = sys.argv[2]
                create_single_ecosystem_video(prompt_key)
            else:
                print("❌ Usage: python sora_enhanced_ecosystem_videos.py single <prompt_key>")
                list_ecosystem_prompts()
        elif command == "all":
            create_ecosystem_sequence()
        else:
            print("❌ Unknown command. Use: list, single <key>, or all")
    else:
        print("🎬 GettingStoned Ecosystem Video Generator")
        print("🚗 The world's first causal navigation system")
        print("\nUsage:")
        print("  python sora_enhanced_ecosystem_videos.py list                    # List all ecosystem prompts")
        print("  python sora_enhanced_ecosystem_videos.py single <prompt_key>     # Create single ecosystem video")
        print("  python sora_enhanced_ecosystem_videos.py all                     # Create all ecosystem videos")
        print("\nExample:")
        print("  python sora_enhanced_ecosystem_videos.py single causal_navigation_system")
        print("\n🚗 Ecosystem videos showcase the complete GettingStoned vision")
