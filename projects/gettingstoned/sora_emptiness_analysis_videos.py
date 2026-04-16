#!/usr/bin/env python3
"""
Sora Emptiness Analysis Videos for GettingStoned App
Showcases the cognitive-awareness tool for cause & effect analysis
"""

import os
import time
import sys
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
openai = OpenAI()

# Emptiness Analysis Video Prompts
EMPTINESS_ANALYSIS_VIDEOS = {
    "cognitive_awareness_tool": {
        "title": "Cognitive Awareness Tool - See the Hidden Structure",
        "prompt": "A person using GettingStoned app, logging a stone for an emotional moment. They tap 'Analyze Cause & Effect' and the app expands into an interactive causal network showing their thoughts, emotions, and reactions. The GettingStoned logo is prominently displayed. The person's face shows curiosity and understanding as they explore the hidden structure behind their experience. Text overlay: 'See the hidden structure behind your thoughts, emotions, and reactions.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "cause_effect_mapping": {
        "title": "Cause & Effect Mapping - Interactive Causal Network",
        "prompt": "A person using GettingStoned's Emptiness Analysis feature, interacting with a dynamic causal network on their phone. The network shows nodes representing conditions like stress, expectation, kindness, empathy, and emotions. The person drags and adjusts nodes to see how changing one condition reshapes the whole event. The GettingStoned logo is clearly visible. The person's expression shows deep understanding and insight. Text overlay: 'Each node represents a condition — stress, expectation, tiredness, kindness, empathy.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "15"
    },
    
    "witness_dissolution": {
        "title": "Witness Dissolution - Seeing Impermanence",
        "prompt": "A person using GettingStoned's Emptiness Analysis, watching as the causal network visually dissolves when they adjust the causes. The 'anger' or 'guilt' nodes lose their solidity as supporting causes are seen clearly. The person's face shows an 'aha' moment of understanding that tension itself is conditional, not absolute. The GettingStoned logo remains visible throughout. Text overlay: 'The network visually dissolves — showing that no single cause or identity is permanent or independent.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "insight_integration": {
        "title": "Insight Integration - From Analysis to Action",
        "prompt": "A person using GettingStoned's Emptiness Analysis, receiving a reflection prompt: 'When this arises again, what condition could you shift first?' The person's face shows clarity and understanding. They save the insight and add a white stone for awareness. The GettingStoned logo is prominently displayed. The person's expression shows transformation from confusion to clarity. Text overlay: 'Understanding that thoughts and emotions are impermanent helps people recover from stress and anger faster.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "10"
    },
    
    "cognitive_dissonance_resolution": {
        "title": "Cognitive Dissonance Resolution - Seeing Interdependence",
        "prompt": "A person using GettingStoned's Emptiness Analysis, exploring a conflict between 'I want to be kind' and 'I lost my temper.' The app shows both sides as interdependent conditions. The person's face shows the tension resolving naturally as they understand both arose from conditions. The GettingStoned logo is clearly visible. The person's expression shows peace and understanding. Text overlay: 'When you can see both sides of a conflict as interdependent, the mind no longer has to force one belief to dominate.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "extremism_softening": {
        "title": "Extremism Softening - Beyond Absolutes",
        "prompt": "A person using GettingStoned's Emptiness Analysis, seeing how their opinions are shaped by context and history. The app reveals the conditions behind their beliefs. The person's face shows softening from rigid thinking to open curiosity. The GettingStoned logo is prominently displayed. The person's expression shows empathy and understanding. Text overlay: 'By revealing that every opinion is shaped by context and history, the app trains users to think less in absolutes.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "10"
    },
    
    "real_curiosity": {
        "title": "Real Curiosity - Exploring How Experiences Form",
        "prompt": "A person using GettingStoned's Emptiness Analysis, exploring how their experiences form rather than labeling them as 'good' or 'bad.' The person's face shows genuine curiosity and learning. The GettingStoned logo is clearly visible. The person's expression shows transformation from judgment to understanding. Text overlay: 'Instead of labeling experiences as good or bad, users explore how experiences form.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "10"
    },
    
    "emotional_resilience": {
        "title": "Emotional Resilience - Clarity Over Suppression",
        "prompt": "A person using GettingStoned's Emptiness Analysis, recovering from stress and anger through understanding impermanence. The person's face shows resilience and clarity rather than suppression. The GettingStoned logo is prominently displayed. The person's expression shows genuine healing and growth. Text overlay: 'Understanding that thoughts and emotions are impermanent helps people recover from stress and anger faster. It's not suppression; it's clarity.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "12"
    },
    
    "perception_transformation": {
        "title": "Perception Transformation - Where Data Meets Awareness",
        "prompt": "A person using GettingStoned's Emptiness Analysis, experiencing the transformation from data tracking to genuine awareness. The app shows how their reflection contributes to a wiser, more nuanced collective Karma Map. The GettingStoned logo is clearly visible. The person's face shows understanding of their role in the broader vision. Text overlay: 'GettingStoned uses technology not just to track ethical behavior, but to transform perception itself.' Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "15"
    },
    
    "emptiness_manifesto": {
        "title": "Emptiness Manifesto - The Engine of Insight",
        "prompt": "A person using GettingStoned's complete Emptiness Analysis system, from logging stones to witnessing dissolution to integrating insights. The GettingStoned logo appears prominently throughout. Text overlay: 'The Emptiness Analysis helps you see that every reaction, belief, or bias is built from parts — and parts can change. Seeing that clearly is the first real step toward peace, inside a person or a planet.' The person's journey shows transformation from confusion to clarity. Shot on iPhone 15 Pro, vertical format 9:16.",
        "duration": "18"
    }
}

def create_emptiness_video(prompt_key, output_dir="./emptiness_analysis_videos"):
    """Create an emptiness analysis video using Sora 2 API"""
    
    if prompt_key not in EMPTINESS_ANALYSIS_VIDEOS:
        print(f"❌ Unknown prompt key: {prompt_key}")
        return None
    
    prompt_data = EMPTINESS_ANALYSIS_VIDEOS[prompt_key]
    
    print(f"🎬 Creating: {prompt_data['title']}")
    print(f"📝 Emptiness Message: {prompt_data['prompt'][:100]}...")
    
    try:
        # Create video with Sora 2
        video = openai.videos.create(
            model="sora-2",
            prompt=prompt_data['prompt'],
            size="720x1280",  # Vertical format for mobile
            seconds=prompt_data['duration']
        )
        
        print(f"✅ Emptiness analysis video generation started: {video.id}")
        return video
        
    except Exception as e:
        print(f"❌ Error creating emptiness analysis video: {e}")
        return None

def monitor_emptiness_video(video_id, output_dir="./emptiness_analysis_videos"):
    """Monitor emptiness analysis video generation progress and download when ready"""
    
    print(f"⏳ Monitoring emptiness analysis video {video_id}...")
    
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
                print(f"\n✅ Emptiness analysis video completed: {video.id}")
                break
            elif video.status == "failed":
                error_msg = getattr(getattr(video, "error", None), "message", "Video generation failed")
                print(f"\n❌ Emptiness analysis video failed: {error_msg}")
                return None
            
            time.sleep(2)
            
        except Exception as e:
            print(f"\n❌ Error monitoring emptiness analysis video: {e}")
            return None
    
    # Download the video
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        content = openai.videos.download_content(video_id, variant="video")
        filename = f"{video_id}_emptiness_analysis_video.mp4"
        filepath = os.path.join(output_dir, filename)
        
        content.write_to_file(filepath)
        print(f"💾 Emptiness analysis video saved: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error downloading emptiness analysis video: {e}")
        return None

def create_emptiness_sequence():
    """Create a sequence of emptiness analysis videos"""
    
    print("🎬 GettingStoned Emptiness Analysis Video Generator")
    print("=" * 50)
    print("🕳 Creating videos for the engine of insight")
    print("🧠 From cognitive awareness to perception transformation")
    print("=" * 50)
    
    # Create output directory
    output_dir = "./emptiness_analysis_videos"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate emptiness analysis videos
    videos = []
    
    for prompt_key in EMPTINESS_ANALYSIS_VIDEOS.keys():
        print(f"\n🎥 Generating: {EMPTINESS_ANALYSIS_VIDEOS[prompt_key]['title']}")
        
        video = create_emptiness_video(prompt_key, output_dir)
        if video:
            videos.append(video)
            time.sleep(3)  # Brief pause between requests
    
    # Monitor all videos
    print(f"\n⏳ Monitoring {len(videos)} emptiness analysis videos...")
    
    completed_videos = []
    for video in videos:
        filepath = monitor_emptiness_video(video.id, output_dir)
        if filepath:
            completed_videos.append(filepath)
    
    print(f"\n✅ Emptiness analysis video generation complete!")
    print(f"📁 Videos saved to: {output_dir}")
    print(f"🎬 Generated {len(completed_videos)} emptiness analysis videos")
    print(f"🕳 Each video showcases the cognitive-awareness tool")
    
    return completed_videos

def create_single_emptiness_video(prompt_key):
    """Create a single emptiness analysis video"""
    
    if prompt_key not in EMPTINESS_ANALYSIS_VIDEOS:
        print(f"❌ Available emptiness analysis prompts: {list(EMPTINESS_ANALYSIS_VIDEOS.keys())}")
        return None
    
    print(f"🎬 Creating emptiness analysis video: {prompt_key}")
    
    video = create_emptiness_video(prompt_key)
    if video:
        return monitor_emptiness_video(video.id)
    
    return None

def list_emptiness_prompts():
    """List all available emptiness analysis video prompts"""
    
    print("📋 Available Emptiness Analysis Video Prompts:")
    print("=" * 50)
    
    for key, data in EMPTINESS_ANALYSIS_VIDEOS.items():
        print(f"\n🎬 {key}")
        print(f"   Title: {data['title']}")
        print(f"   Duration: {data['duration']} seconds")
        print(f"   Message: {data['prompt'][:80]}...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            list_emptiness_prompts()
        elif command == "single":
            if len(sys.argv) > 2:
                prompt_key = sys.argv[2]
                create_single_emptiness_video(prompt_key)
            else:
                print("❌ Usage: python sora_emptiness_analysis_videos.py single <prompt_key>")
                list_emptiness_prompts()
        elif command == "all":
            create_emptiness_sequence()
        else:
            print("❌ Unknown command. Use: list, single <key>, or all")
    else:
        print("🎬 GettingStoned Emptiness Analysis Video Generator")
        print("🕳 The engine of insight")
        print("\nUsage:")
        print("  python sora_emptiness_analysis_videos.py list                    # List all emptiness analysis prompts")
        print("  python sora_emptiness_analysis_videos.py single <prompt_key>     # Create single emptiness analysis video")
        print("  python sora_emptiness_analysis_videos.py all                     # Create all emptiness analysis videos")
        print("\nExample:")
        print("  python sora_emptiness_analysis_videos.py single cognitive_awareness_tool")
        print("\n🕳 Emptiness analysis videos showcase the cognitive-awareness tool")
