#!/usr/bin/env python3
"""
Audio Enhancement for GettingStoned Marketing Videos
Adds music, voiceovers, and sound effects to enhance video impact
"""

import os
import subprocess
from pathlib import Path

# Audio enhancement configuration
AUDIO_CONFIG = {
    "music_tracks": {
        "meditation": "meditation_ambient.mp3",
        "karma": "karma_visualization.mp3", 
        "stone_logging": "stone_drop_sounds.mp3",
        "manifesto": "spiritual_inspiration.mp3"
    },
    
    "voiceover_scripts": {
        "app_intro": "Transform your daily actions into spiritual practice with GettingStoned",
        "stone_demo": "Log white stones for virtuous acts, black stones for non-virtuous ones",
        "karma_viz": "Watch your karma transform through data visualization",
        "meditation": "Track your meditation practice with ancient wisdom",
        "cta": "Download GettingStoned and begin your journey to awareness"
    },
    
    "sound_effects": {
        "stone_drop": "stone_drop.wav",
        "meditation_bell": "meditation_bell.wav",
        "app_notification": "app_notification.wav",
        "karma_complete": "karma_complete.wav"
    }
}

def add_background_music(video_path, music_track, output_path):
    """Add background music to video"""
    try:
        cmd = [
            "ffmpeg", "-i", video_path, "-i", music_track,
            "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first",
            "-c:v", "copy", "-shortest", output_path
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Added background music: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error adding music: {e}")
        return False

def add_voiceover(video_path, voiceover_text, output_path):
    """Add AI-generated voiceover to video"""
    try:
        # Generate voiceover using text-to-speech
        voiceover_cmd = [
            "say", "-v", "Samantha", "-o", "temp_voiceover.aiff", voiceover_text
        ]
        subprocess.run(voiceover_cmd, check=True)
        
        # Combine video with voiceover
        combine_cmd = [
            "ffmpeg", "-i", video_path, "-i", "temp_voiceover.aiff",
            "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first",
            "-c:v", "copy", "-shortest", output_path
        ]
        subprocess.run(combine_cmd, check=True)
        
        # Clean up temp file
        os.remove("temp_voiceover.aiff")
        print(f"✅ Added voiceover: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error adding voiceover: {e}")
        return False

def add_sound_effects(video_path, sound_effect, output_path):
    """Add sound effects to video"""
    try:
        cmd = [
            "ffmpeg", "-i", video_path, "-i", sound_effect,
            "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first",
            "-c:v", "copy", "-shortest", output_path
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Added sound effects: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error adding sound effects: {e}")
        return False

def enhance_video(video_path, enhancement_type="music"):
    """Enhance video with audio based on type"""
    video_name = Path(video_path).stem
    output_path = f"enhanced_{video_name}.mp4"
    
    if enhancement_type == "music":
        # Add meditation music for spiritual content
        return add_background_music(video_path, "meditation_ambient.mp3", output_path)
    elif enhancement_type == "voiceover":
        # Add voiceover for educational content
        return add_voiceover(video_path, AUDIO_CONFIG["voiceover_scripts"]["app_intro"], output_path)
    elif enhancement_type == "sound_effects":
        # Add stone drop sounds for stone logging videos
        return add_sound_effects(video_path, "stone_drop.wav", output_path)
    
    return False

def enhance_all_videos():
    """Enhance all generated videos with appropriate audio"""
    video_dirs = [
        "screenshot_enhanced_videos",
        "ten_non_virtues_videos", 
        "cta_videos"
    ]
    
    for video_dir in video_dirs:
        if os.path.exists(video_dir):
            print(f"🎵 Enhancing videos in {video_dir}/")
            for video_file in os.listdir(video_dir):
                if video_file.endswith('.mp4'):
                    video_path = os.path.join(video_dir, video_file)
                    
                    # Determine enhancement type based on video content
                    if "stone_logging" in video_file:
                        enhance_video(video_path, "sound_effects")
                    elif "karma" in video_file or "meditation" in video_file:
                        enhance_video(video_path, "music")
                    elif "cta" in video_file:
                        enhance_video(video_path, "voiceover")
                    else:
                        enhance_video(video_path, "music")

if __name__ == "__main__":
    print("🎵 Starting audio enhancement for GettingStoned videos...")
    enhance_all_videos()
    print("✅ Audio enhancement complete!")

