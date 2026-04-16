#!/usr/bin/env python3
"""
Social Media Deployment for GettingStoned Marketing Videos
Automates posting to various social media platforms
"""

import os
import json
from pathlib import Path
from datetime import datetime, timedelta

# Social media platform configurations
PLATFORM_CONFIG = {
    "instagram": {
        "max_duration": 60,
        "aspect_ratio": "9:16",
        "hashtags": ["#GettingStoned", "#Meditation", "#Mindfulness", "#SpiritualTech", "#Karma", "#Buddhism", "#AI", "#TechForGood"],
        "posting_times": ["09:00", "12:00", "15:00", "18:00"]
    },
    
    "tiktok": {
        "max_duration": 60,
        "aspect_ratio": "9:16", 
        "hashtags": ["#GettingStoned", "#Meditation", "#Mindfulness", "#SpiritualTech", "#Karma", "#Buddhism", "#AI", "#TechForGood", "#FYP"],
        "posting_times": ["10:00", "14:00", "16:00", "20:00"]
    },
    
    "youtube": {
        "max_duration": 300,
        "aspect_ratio": "16:9",
        "hashtags": ["GettingStoned", "Meditation", "Mindfulness", "SpiritualTech", "Karma", "Buddhism", "AI", "TechForGood"],
        "posting_times": ["11:00", "15:00", "19:00"]
    },
    
    "facebook": {
        "max_duration": 240,
        "aspect_ratio": "16:9",
        "hashtags": ["#GettingStoned", "#Meditation", "#Mindfulness", "#SpiritualTech", "#Karma", "#Buddhism", "#AI", "#TechForGood"],
        "posting_times": ["09:00", "13:00", "17:00", "21:00"]
    },
    
    "linkedin": {
        "max_duration": 300,
        "aspect_ratio": "16:9",
        "hashtags": ["GettingStoned", "Meditation", "Mindfulness", "SpiritualTech", "Karma", "Buddhism", "AI", "TechForGood", "Innovation"],
        "posting_times": ["08:00", "12:00", "16:00"]
    }
}

# Content templates for different video types
CONTENT_TEMPLATES = {
    "app_launch": {
        "title": "Introducing GettingStoned: The Spiritual Technology Revolution",
        "description": "Transform your daily actions into spiritual practice with GettingStoned. Ancient wisdom meets modern technology. 🪨✨ #GettingStoned #SpiritualTech #Meditation #Mindfulness",
        "call_to_action": "Download GettingStoned and begin your journey to awareness"
    },
    
    "stone_logging": {
        "title": "Log Your Karma with Digital Stones",
        "description": "White stones for virtuous acts, black stones for non-virtuous ones. Track your spiritual progress with GettingStoned. 🪨⚪⚫ #Karma #SpiritualPractice #GettingStoned",
        "call_to_action": "Start logging your spiritual journey today"
    },
    
    "ten_non_virtues": {
        "title": "The Ten Non-Virtues: A Digital Path to Awareness",
        "description": "Explore the ancient Buddhist teachings through modern technology. Each non-virtue becomes a learning opportunity. 🧘‍♀️📱 #Buddhism #Mindfulness #GettingStoned #SpiritualGrowth",
        "call_to_action": "Discover your path to spiritual awareness"
    },
    
    "karma_visualization": {
        "title": "See Your Karma Transform Through Data",
        "description": "Watch your spiritual progress unfold with beautiful data visualizations. Karma becomes visible, measurable, and transformative. 📊✨ #Karma #DataViz #SpiritualTech #GettingStoned",
        "call_to_action": "Visualize your spiritual journey"
    },
    
    "meditation_tracking": {
        "title": "Meditation Meets Technology",
        "description": "Track your meditation practice with ancient wisdom and modern insights. Every session builds toward enlightenment. 🧘‍♂️📱 #Meditation #Mindfulness #GettingStoned #SpiritualPractice",
        "call_to_action": "Begin your meditation journey"
    }
}

def create_posting_schedule():
    """Create a 30-day posting schedule for all videos"""
    schedule = []
    start_date = datetime.now()
    
    # Video types and their optimal posting days
    video_schedule = [
        ("app_launch", 0),      # Day 1
        ("stone_logging", 2),    # Day 3
        ("karma_visualization", 5), # Day 6
        ("meditation_tracking", 8), # Day 9
        ("ten_non_virtues", 12), # Day 13 (start of series)
        ("feature_showcase", 15), # Day 16
        ("manifesto", 18),       # Day 19
        ("cta_series", 22),      # Day 23
        ("user_journey", 25),    # Day 26
        ("final_launch", 29)     # Day 30
    ]
    
    for video_type, day_offset in video_schedule:
        post_date = start_date + timedelta(days=day_offset)
        schedule.append({
            "date": post_date.strftime("%Y-%m-%d"),
            "video_type": video_type,
            "platforms": ["instagram", "tiktok", "youtube", "facebook", "linkedin"],
            "content": CONTENT_TEMPLATES.get(video_type, CONTENT_TEMPLATES["app_launch"])
        })
    
    return schedule

def generate_platform_specific_content(video_type, platform):
    """Generate platform-specific content for each video"""
    base_content = CONTENT_TEMPLATES.get(video_type, CONTENT_TEMPLATES["app_launch"])
    platform_config = PLATFORM_CONFIG[platform]
    
    # Adjust content for platform
    if platform == "tiktok":
        # Shorter, more engaging content for TikTok
        content = {
            "title": base_content["title"][:50] + "...",
            "description": base_content["description"][:200] + "...",
            "hashtags": platform_config["hashtags"][:5]  # Limit hashtags for TikTok
        }
    elif platform == "linkedin":
        # Professional tone for LinkedIn
        content = {
            "title": base_content["title"],
            "description": f"Professional insight: {base_content['description']}",
            "hashtags": platform_config["hashtags"]
        }
    else:
        # Standard content for other platforms
        content = {
            "title": base_content["title"],
            "description": base_content["description"],
            "hashtags": platform_config["hashtags"]
        }
    
    return content

def create_deployment_plan():
    """Create a comprehensive deployment plan"""
    schedule = create_posting_schedule()
    
    deployment_plan = {
        "campaign_name": "GettingStoned Launch Campaign",
        "duration": "30 days",
        "total_videos": len(schedule),
        "platforms": list(PLATFORM_CONFIG.keys()),
        "schedule": schedule,
        "metrics": {
            "target_views": 100000,
            "target_engagement": 5.0,
            "target_downloads": 1000
        }
    }
    
    return deployment_plan

def save_deployment_plan(plan):
    """Save deployment plan to JSON file"""
    with open("deployment_plan.json", "w") as f:
        json.dump(plan, f, indent=2)
    print("✅ Deployment plan saved to deployment_plan.json")

def generate_social_media_posts():
    """Generate all social media posts for the campaign"""
    plan = create_deployment_plan()
    
    posts = []
    for schedule_item in plan["schedule"]:
        for platform in schedule_item["platforms"]:
            content = generate_platform_specific_content(
                schedule_item["video_type"], 
                platform
            )
            
            post = {
                "date": schedule_item["date"],
                "platform": platform,
                "video_type": schedule_item["video_type"],
                "content": content,
                "posting_time": PLATFORM_CONFIG[platform]["posting_times"][0]
            }
            posts.append(post)
    
    return posts

def main():
    """Main deployment function"""
    print("🚀 Creating GettingStoned Social Media Deployment Plan...")
    
    # Create deployment plan
    plan = create_deployment_plan()
    save_deployment_plan(plan)
    
    # Generate all posts
    posts = generate_social_media_posts()
    
    # Save posts to file
    with open("social_media_posts.json", "w") as f:
        json.dump(posts, f, indent=2)
    
    print(f"✅ Generated {len(posts)} social media posts")
    print(f"📅 Campaign duration: {plan['duration']}")
    print(f"🎯 Target platforms: {', '.join(plan['platforms'])}")
    print(f"📊 Target metrics: {plan['metrics']['target_views']} views, {plan['metrics']['target_engagement']}% engagement")
    
    print("\n🎬 Next Steps:")
    print("1. Review deployment_plan.json")
    print("2. Review social_media_posts.json") 
    print("3. Set up social media accounts")
    print("4. Schedule posts using your preferred tool")
    print("5. Monitor performance and adjust strategy")

if __name__ == "__main__":
    main()





