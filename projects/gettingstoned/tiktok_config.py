#!/usr/bin/env python3
"""
TikTok Configuration for GettingStoned Marketing
Optimized content templates and posting strategies
"""

# TikTok-specific content optimization
TIKTOK_CONTENT_STRATEGY = {
    "optimal_length": "15-30 seconds",
    "aspect_ratio": "9:16",
    "max_caption_length": 2200,
    "optimal_hashtags": 3-5,
    "best_posting_times": ["10:00", "14:00", "16:00", "20:00"]
}

# GettingStoned-specific content templates
CONTENT_TEMPLATES = {
    "app_launch": {
        "hook": "POV: You discover the app that transforms your daily actions into spiritual practice",
        "caption": "GettingStoned: Where ancient wisdom meets modern technology 🪨✨\n\nTrack your karma, log your stones, and watch your spiritual journey unfold through beautiful data visualizations.\n\n#GettingStoned #SpiritualTech #Meditation #Mindfulness #Karma #Buddhism #AI #TechForGood #FYP",
        "hashtags": ["GettingStoned", "SpiritualTech", "Meditation", "Mindfulness", "Karma", "Buddhism", "AI", "TechForGood", "FYP"],
        "call_to_action": "Download GettingStoned and begin your journey to awareness"
    },
    
    "stone_logging": {
        "hook": "This app lets you log your karma with digital stones",
        "caption": "White stones for virtuous acts, black stones for non-virtuous ones 🪨⚪⚫\n\nTrack your spiritual progress and see your karma transform through data.\n\n#GettingStoned #Karma #SpiritualPractice #Meditation #Mindfulness #Buddhism #AI #TechForGood #FYP",
        "hashtags": ["GettingStoned", "Karma", "SpiritualPractice", "Meditation", "Mindfulness", "Buddhism", "AI", "TechForGood", "FYP"],
        "call_to_action": "Start logging your spiritual journey today"
    },
    
    "ten_non_virtues": {
        "hook": "The Ten Non-Virtues: A digital path to awareness",
        "caption": "Explore ancient Buddhist teachings through modern technology 🧘‍♀️📱\n\nEach non-virtue becomes a learning opportunity for growth.\n\n#GettingStoned #Buddhism #Mindfulness #SpiritualGrowth #Meditation #Karma #AI #TechForGood #FYP",
        "hashtags": ["GettingStoned", "Buddhism", "Mindfulness", "SpiritualGrowth", "Meditation", "Karma", "AI", "TechForGood", "FYP"],
        "call_to_action": "Discover your path to spiritual awareness"
    },
    
    "karma_visualization": {
        "hook": "Watch your karma transform through beautiful data",
        "caption": "See your spiritual progress unfold with stunning visualizations 📊✨\n\nKarma becomes visible, measurable, and transformative.\n\n#GettingStoned #Karma #DataViz #SpiritualTech #Meditation #Mindfulness #Buddhism #AI #TechForGood #FYP",
        "hashtags": ["GettingStoned", "Karma", "DataViz", "SpiritualTech", "Meditation", "Mindfulness", "Buddhism", "AI", "TechForGood", "FYP"],
        "call_to_action": "Visualize your spiritual journey"
    },
    
    "meditation_tracking": {
        "hook": "Meditation meets technology in the most beautiful way",
        "caption": "Track your meditation practice with ancient wisdom and modern insights 🧘‍♂️📱\n\nEvery session builds toward enlightenment.\n\n#GettingStoned #Meditation #Mindfulness #SpiritualPractice #Karma #Buddhism #AI #TechForGood #FYP",
        "hashtags": ["GettingStoned", "Meditation", "Mindfulness", "SpiritualPractice", "Karma", "Buddhism", "AI", "TechForGood", "FYP"],
        "call_to_action": "Begin your meditation journey"
    },
    
    "feature_showcase": {
        "hook": "This app has features you never knew you needed",
        "caption": "From AR stone placement to EEG integration - GettingStoned is revolutionizing spiritual practice 🚀\n\nSee how technology enhances ancient wisdom.\n\n#GettingStoned #SpiritualTech #Innovation #Meditation #Mindfulness #Karma #Buddhism #AI #TechForGood #FYP",
        "hashtags": ["GettingStoned", "SpiritualTech", "Innovation", "Meditation", "Mindfulness", "Karma", "Buddhism", "AI", "TechForGood", "FYP"],
        "call_to_action": "Experience the future of spiritual practice"
    }
}

# TikTok posting strategy
POSTING_STRATEGY = {
    "frequency": "2-3 posts per day",
    "optimal_times": {
        "morning": "10:00 AM",
        "afternoon": "2:00 PM", 
        "evening": "8:00 PM"
    },
    "content_mix": {
        "educational": 40,  # Ten non-virtues, meditation tips
        "feature_showcase": 30,  # App features, demos
        "inspirational": 20,  # Manifesto, philosophy
        "call_to_action": 10   # Download prompts
    }
}

# Engagement optimization
ENGAGEMENT_TACTICS = {
    "hooks": [
        "POV: You discover the app that...",
        "This app lets you...",
        "The Ten Non-Virtues: A digital path to...",
        "Watch your karma transform through...",
        "Meditation meets technology in...",
        "This app has features you never knew...",
        "What if I told you there's an app that...",
        "The spiritual practice you never knew you needed..."
    ],
    
    "trending_sounds": [
        "Meditation music",
        "Ambient sounds",
        "Nature sounds",
        "Buddhist chants",
        "Minimalist beats"
    ],
    
    "visual_elements": [
        "App screenshots",
        "Data visualizations", 
        "Meditation scenes",
        "Stone imagery",
        "Karma charts"
    ]
}

# Analytics tracking
ANALYTICS_METRICS = {
    "primary": [
        "views",
        "likes", 
        "comments",
        "shares",
        "saves"
    ],
    "secondary": [
        "completion_rate",
        "engagement_rate",
        "click_through_rate",
        "download_conversions"
    ],
    "targets": {
        "views_per_video": 10000,
        "engagement_rate": 5.0,
        "completion_rate": 80.0,
        "download_conversions": 2.0
    }
}

def get_optimized_caption(video_type, custom_hook=None):
    """Get optimized caption for TikTok"""
    template = CONTENT_TEMPLATES.get(video_type, CONTENT_TEMPLATES["app_launch"])
    
    hook = custom_hook or template["hook"]
    caption = template["caption"]
    hashtags = " ".join([f"#{tag}" for tag in template["hashtags"]])
    
    return f"{hook}\n\n{caption}\n\n{hashtags}"

def get_posting_schedule(days=30, videos_per_day=2):
    """Generate optimized posting schedule"""
    import random
    from datetime import datetime, timedelta
    
    schedule = []
    start_date = datetime.now()
    
    video_types = list(CONTENT_TEMPLATES.keys())
    
    for day in range(days):
        current_date = start_date + timedelta(days=day)
        
        # Select video types for the day
        daily_videos = random.sample(video_types, min(videos_per_day, len(video_types)))
        
        # Select posting times
        posting_times = random.sample(TIKTOK_CONTENT_STRATEGY["best_posting_times"], 
                                    min(videos_per_day, len(TIKTOK_CONTENT_STRATEGY["best_posting_times"])))
        
        day_schedule = {
            "date": current_date.strftime("%Y-%m-%d"),
            "videos": []
        }
        
        for i, video_type in enumerate(daily_videos):
            day_schedule["videos"].append({
                "type": video_type,
                "posting_time": posting_times[i] if i < len(posting_times) else posting_times[0],
                "caption": get_optimized_caption(video_type),
                "hashtags": CONTENT_TEMPLATES[video_type]["hashtags"]
            })
        
        schedule.append(day_schedule)
    
    return schedule

if __name__ == "__main__":
    # Generate sample posting schedule
    schedule = get_posting_schedule(days=7, videos_per_day=2)
    
    print("📅 Sample TikTok Posting Schedule:")
    for day in schedule:
        print(f"\n📅 {day['date']}")
        for video in day['videos']:
            print(f"  🕐 {video['posting_time']} - {video['type']}")
            print(f"     📝 {video['caption'][:100]}...")
            print(f"     #️⃣ {', '.join(video['hashtags'][:5])}...")


