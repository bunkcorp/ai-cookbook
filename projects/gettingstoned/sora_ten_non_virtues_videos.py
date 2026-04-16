#!/usr/bin/env python3
"""
Sora Ten Non-Virtues Videos for GettingStoned App
Cinematic timelapse series showing transformation through awareness
"""

import os
import time
import sys
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
openai = OpenAI()

# Ten Non-Virtues Video Prompts
TEN_NON_VIRTUES_VIDEOS = {
    "killing_harm": {
        "title": "Killing Harm - From Destruction to Care",
        "prompt": "A 100-frame cinematic time-lapse showing a person gradually giving up harmful impulses. Early frames: they crush insects or break objects without thought; each act logs a ⚫ Black Stone in the GettingStoned app. Split screen: right shows black-stone accumulation curve (gamma-shaped). Around frame 60 they notice the impulse, pause, meditate, and log a ⚪ White Stone. By frame 100 the curve declines and stones dissolve into light. End with the person calmly watering plants, warm light filling the room, graph flattening, text: 'Karma exhausted — awareness remains.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "15"
    },
    
    "harsh_speech": {
        "title": "Harsh Speech - From Anger to Gentleness",
        "prompt": "Time-lapse of a person overcoming harsh or angry speech. Early frames: quick-cut arguments and texts with sharp words; each logs a ⚫ Black Stone. After frame 60 they reread their words, breathe, and log a ⚪ White Stone. Graph peaks then declines. Final frames: gentle conversation under golden light, stones dissolve, caption: 'Speech refined — peace revealed.' The GettingStoned logo is prominently displayed on the phone screen. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "gossip_idle_talk": {
        "title": "Gossip & Idle Talk - From Noise to Silence",
        "prompt": "A person repeatedly spreads gossip; the phone buzzes, they log ⚫ Black Stones. Graph on the right rises. Around frame 70 they meditate, then choose silence and log a ⚪ White Stone. By frame 100 the curve stabilizes; warm light fills the scene. End text: 'Truth spoken softly; awareness remains.' The GettingStoned logo is clearly visible on the phone interface. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "stealing": {
        "title": "Stealing - From Taking to Giving",
        "prompt": "Short film of a person overcoming dishonest taking. Early scenes: they take items without asking; each act triggers ⚫ Black Stone log. Gamma curve rises. After frame 60 they pause, return an item, log ⚪ White Stone. Curve falls, stones glow, fade to golden peace and caption: 'Generosity replaces grasping.' The GettingStoned logo is prominently displayed throughout. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "sexual_misconduct": {
        "title": "Sexual Misconduct - From Carelessness to Respect",
        "prompt": "Symbolic time-lapse: person acts carelessly in relationships, logging ⚫ Black Stones for broken trust. Midway they meditate, offer apology, log ⚪ White Stone. Graph peaks then smooths. Final scene: respectful connection and warmth; stones dissolve; caption: 'Respect restores harmony — awareness remains.' The GettingStoned logo is clearly visible on the phone screen. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "greed_covetousness": {
        "title": "Greed & Covetousness - From Grasping to Contentment",
        "prompt": "Story of letting go of greed. Early: person obsessively checks possessions, logging ⚫ Black Stones. Graph climbs fast. After awareness, they share or donate, logging ⚪ White Stone. Curve declines; room brightens. End with open window and breeze: 'Contentment frees the mind.' The GettingStoned logo is prominently displayed on the phone interface. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "anger_hatred": {
        "title": "Anger & Hatred - From Fire to Patience",
        "prompt": "Person succumbs to anger, throwing objects, logging ⚫ Black Stones. Graph spikes like flame. Around frame 60 they pause, meditate, log ⚪ White Stone. Color shifts red→amber; curve falls. End with smile and calm light: 'Patience cools the fire — awareness remains.' The GettingStoned logo is clearly visible on the phone screen. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "wrong_view": {
        "title": "Wrong View - From Rigidity to Wisdom",
        "prompt": "Person clings to rigid opinions, arguing online; each act logs a ⚫ Black Stone. Split-screen graph loops upward. After meditation at frame 70, thoughts realign, log ⚪ White Stone. Curve evens out; final scene serene and balanced: 'Seeing through extremes, peace unfolds.' The GettingStoned logo is prominently displayed on the phone interface. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "deceit_lying": {
        "title": "Deceit & Lying - From Falsehood to Truth",
        "prompt": "Person tells small lies; each time logs a ⚫ Black Stone. Graph rises; reflection begins at frame 60. They tell the truth, log ⚪ White Stone, graph declines. Light warms; stones dissolve; caption: 'Honesty clears the path — karma balanced.' The GettingStoned logo is clearly visible on the phone screen. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "envy_jealousy": {
        "title": "Envy & Jealousy - From Comparison to Joy",
        "prompt": "Person compares themselves to others, logging ⚫ Black Stones as envy appears. Graph builds then softens as gratitude practice begins. By frame 100 curve levels; white stones float upward, sunlight fills room. Text: 'Rejoicing in others' joy, the heart becomes light.' The GettingStoned logo is prominently displayed throughout. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    }
}

def create_non_virtue_video(prompt_key, output_dir="./ten_non_virtues_videos"):
    """Create a ten non-virtues video using Sora 2 API"""
    
    if prompt_key not in TEN_NON_VIRTUES_VIDEOS:
        print(f"❌ Unknown prompt key: {prompt_key}")
        return None
    
    prompt_data = TEN_NON_VIRTUES_VIDEOS[prompt_key]
    
    print(f"🎬 Creating: {prompt_data['title']}")
    print(f"📝 Non-Virtue Message: {prompt_data['prompt'][:100]}...")
    
    try:
        # Create video with Sora 2
        video = openai.videos.create(
            model="sora-2",
            prompt=prompt_data['prompt'],
            size="720x1280",  # Vertical format for mobile
            seconds=prompt_data['duration']
        )
        
        print(f"✅ Ten non-virtues video generation started: {video.id}")
        return video
        
    except Exception as e:
        print(f"❌ Error creating ten non-virtues video: {e}")
        return None

def monitor_non_virtue_video(video_id, output_dir="./ten_non_virtues_videos"):
    """Monitor ten non-virtues video generation progress and download when ready"""
    
    print(f"⏳ Monitoring ten non-virtues video {video_id}...")
    
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
                print(f"\n✅ Ten non-virtues video completed: {video.id}")
                break
            elif video.status == "failed":
                error_msg = getattr(getattr(video, "error", None), "message", "Video generation failed")
                print(f"\n❌ Ten non-virtues video failed: {error_msg}")
                return None
            
            time.sleep(2)
            
        except Exception as e:
            print(f"\n❌ Error monitoring ten non-virtues video: {e}")
            return None
    
    # Download the video
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        content = openai.videos.download_content(video_id, variant="video")
        filename = f"{video_id}_ten_non_virtues_video.mp4"
        filepath = os.path.join(output_dir, filename)
        
        content.write_to_file(filepath)
        print(f"💾 Ten non-virtues video saved: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error downloading ten non-virtues video: {e}")
        return None

def create_ten_non_virtues_sequence():
    """Create a sequence of ten non-virtues videos"""
    
    print("🎬 GettingStoned Ten Non-Virtues Video Generator")
    print("=" * 50)
    print("🪨 Creating cinematic timelapse series")
    print("⚫⚪ From non-virtue to virtue through awareness")
    print("=" * 50)
    
    # Create output directory
    output_dir = "./ten_non_virtues_videos"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate ten non-virtues videos
    videos = []
    
    for prompt_key in TEN_NON_VIRTUES_VIDEOS.keys():
        title = TEN_NON_VIRTUES_VIDEOS[prompt_key]["title"]
        print(f"\n🎥 Generating: {title}")
        video = create_non_virtue_video(prompt_key, output_dir)
        if video:
            videos.append(video)
            time.sleep(3)  # Brief pause between requests
    
    # Monitor all videos
    print(f"\n⏳ Monitoring {len(videos)} ten non-virtues videos...")
    
    completed_videos = []
    for video in videos:
        filepath = monitor_non_virtue_video(video.id, output_dir)
        if filepath:
            completed_videos.append(filepath)
    
    print(f"\n✅ Ten non-virtues video generation complete!")
    print(f"📁 Videos saved to: {output_dir}")
    print(f"🎬 Generated {len(completed_videos)} ten non-virtues videos")
    print(f"🪨 Each video shows transformation through awareness")
    
    return completed_videos

def create_single_non_virtue_video(prompt_key):
    """Create a single ten non-virtues video"""
    
    if prompt_key not in TEN_NON_VIRTUES_VIDEOS:
        print(f"❌ Available ten non-virtues prompts: {list(TEN_NON_VIRTUES_VIDEOS.keys())}")
        return None
    
    print(f"🎬 Creating ten non-virtues video: {prompt_key}")
    
    video = create_non_virtue_video(prompt_key)
    if video:
        return monitor_non_virtue_video(video.id)
    
    return None

def list_ten_non_virtues_prompts():
    """List all available ten non-virtues video prompts"""
    
    print("📋 Available Ten Non-Virtues Video Prompts:")
    print("=" * 50)
    
    for key, data in TEN_NON_VIRTUES_VIDEOS.items():
        print(f"\n🎬 {key}")
        print(f"   Title: {data['title']}")
        print(f"   Duration: {data['duration']} seconds")
        print(f"   Message: {data['prompt'][:80]}...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            list_ten_non_virtues_prompts()
        elif command == "single":
            if len(sys.argv) > 2:
                prompt_key = sys.argv[2]
                create_single_non_virtue_video(prompt_key)
            else:
                print("❌ Usage: python sora_ten_non_virtues_videos.py single <prompt_key>")
                list_ten_non_virtues_prompts()
        elif command == "all":
            create_ten_non_virtues_sequence()
        else:
            print("❌ Unknown command. Use: list, single <key>, or all")
    else:
        print("🎬 GettingStoned Ten Non-Virtues Video Generator")
        print("🪨 Cinematic timelapse series")
        print("\nUsage:")
        print("  python sora_ten_non_virtues_videos.py list                    # List all ten non-virtues prompts")
        print("  python sora_ten_non_virtues_videos.py single <prompt_key>     # Create single ten non-virtues video")
        print("  python sora_ten_non_virtues_videos.py all                     # Create all ten non-virtues videos")
        print("\nExample:")
        print("  python sora_ten_non_virtues_videos.py single killing_harm")
        print("\n🪨 Ten non-virtues videos showcase transformation through awareness")
