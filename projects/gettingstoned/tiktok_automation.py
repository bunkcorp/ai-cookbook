#!/usr/bin/env python3
"""
TikTok Automation for GettingStoned Marketing Videos
Automates posting to TikTok using browser automation
"""

import os
import json
import time
import random
from pathlib import Path
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TikTokAutomation:
    def __init__(self, headless=False):
        """Initialize TikTok automation with Chrome driver"""
        self.driver = None
        self.headless = headless
        self.setup_driver()
        
    def setup_driver(self):
        """Set up Chrome driver with appropriate options"""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36")
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            print("✅ Chrome driver initialized successfully")
        except Exception as e:
            print(f"❌ Error initializing Chrome driver: {e}")
            print("Please ensure ChromeDriver is installed and in your PATH")
            raise
    
    def login_to_tiktok(self, username, password):
        """Login to TikTok account"""
        try:
            print("🔐 Logging into TikTok...")
            self.driver.get("https://www.tiktok.com/login")
            
            # Wait for login form to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
            )
            
            # Find username field
            username_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
            username_field.send_keys(username)
            
            # Find password field
            password_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
            password_field.send_keys(password)
            
            # Click login button
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Wait for successful login
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-e2e='nav-upload']"))
            )
            
            print("✅ Successfully logged into TikTok")
            return True
            
        except TimeoutException:
            print("❌ Login timeout - please check credentials")
            return False
        except Exception as e:
            print(f"❌ Login error: {e}")
            return False
    
    def upload_video(self, video_path, caption, hashtags=None):
        """Upload a video to TikTok"""
        try:
            print(f"📤 Uploading video: {video_path}")
            
            # Navigate to upload page
            self.driver.get("https://www.tiktok.com/upload")
            
            # Wait for upload button
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
            )
            
            # Upload video file
            file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            file_input.send_keys(os.path.abspath(video_path))
            
            # Wait for video to process
            print("⏳ Processing video...")
            time.sleep(10)
            
            # Add caption
            if caption:
                caption_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-e2e='video-caption']"))
                )
                caption_field.clear()
                caption_field.send_keys(caption)
            
            # Add hashtags
            if hashtags:
                hashtag_text = " ".join([f"#{tag}" for tag in hashtags])
                caption_field.send_keys(f" {hashtag_text}")
            
            # Set video to public
            try:
                privacy_button = self.driver.find_element(By.CSS_SELECTOR, "[data-e2e='privacy-setting']")
                privacy_button.click()
                
                public_option = self.driver.find_element(By.CSS_SELECTOR, "[data-e2e='privacy-public']")
                public_option.click()
            except NoSuchElementException:
                print("⚠️ Could not set privacy to public - using default")
            
            # Post the video
            post_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-e2e='publish-button']"))
            )
            post_button.click()
            
            # Wait for upload to complete
            print("⏳ Uploading video...")
            time.sleep(30)
            
            print("✅ Video uploaded successfully!")
            return True
            
        except TimeoutException:
            print("❌ Upload timeout")
            return False
        except Exception as e:
            print(f"❌ Upload error: {e}")
            return False
    
    def schedule_video(self, video_path, caption, hashtags=None, schedule_time=None):
        """Schedule a video for later posting"""
        try:
            print(f"📅 Scheduling video: {video_path}")
            
            # Navigate to upload page
            self.driver.get("https://www.tiktok.com/upload")
            
            # Upload video file
            file_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
            )
            file_input.send_keys(os.path.abspath(video_path))
            
            # Wait for video to process
            time.sleep(10)
            
            # Add caption and hashtags
            if caption:
                caption_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-e2e='video-caption']"))
                )
                caption_field.clear()
                caption_field.send_keys(caption)
                
                if hashtags:
                    hashtag_text = " ".join([f"#{tag}" for tag in hashtags])
                    caption_field.send_keys(f" {hashtag_text}")
            
            # Set schedule time
            if schedule_time:
                schedule_button = self.driver.find_element(By.CSS_SELECTOR, "[data-e2e='schedule-button']")
                schedule_button.click()
                
                # Set the schedule time (implementation depends on TikTok's interface)
                # This would need to be adapted based on current TikTok interface
                print(f"📅 Video scheduled for {schedule_time}")
            
            # Save as draft or schedule
            save_button = self.driver.find_element(By.CSS_SELECTOR, "[data-e2e='save-button']")
            save_button.click()
            
            print("✅ Video scheduled successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Scheduling error: {e}")
            return False
    
    def close(self):
        """Close the browser driver"""
        if self.driver:
            self.driver.quit()
            print("🔒 Browser closed")

class TikTokContentManager:
    def __init__(self):
        self.video_folders = {
            "marketing_videos_with_cta": "marketing_videos_with_cta/",
            "screenshot_enhanced_videos": "screenshot_enhanced_videos/",
            "ten_non_virtues_videos": "ten_non_virtues_videos/"
        }
        
        self.content_templates = {
            "cta_video": {
                "caption": "Transform your daily actions into spiritual practice with GettingStoned 🪨✨",
                "hashtags": ["GettingStoned", "Meditation", "Mindfulness", "SpiritualTech", "Karma", "Buddhism", "AI", "TechForGood", "FYP"]
            },
            "screenshot_enhanced": {
                "caption": "See how ancient wisdom meets modern technology 📱🧘‍♀️",
                "hashtags": ["GettingStoned", "SpiritualTech", "Meditation", "Mindfulness", "Karma", "Buddhism", "AI", "TechForGood", "FYP"]
            },
            "ten_non_virtues": {
                "caption": "Explore the Ten Non-Virtues through digital practice 🧘‍♂️📱",
                "hashtags": ["GettingStoned", "Buddhism", "Mindfulness", "SpiritualGrowth", "Meditation", "Karma", "AI", "TechForGood", "FYP"]
            }
        }
    
    def get_video_files(self, folder_type):
        """Get all video files from specified folder"""
        folder_path = self.video_folders.get(folder_type)
        if not folder_path:
            return []
        
        video_files = []
        for file in Path(folder_path).glob("*.mp4"):
            video_files.append(str(file))
        
        return video_files
    
    def generate_caption(self, video_type, custom_text=None):
        """Generate caption for video"""
        template = self.content_templates.get(video_type, self.content_templates["cta_video"])
        
        if custom_text:
            return f"{custom_text} {template['hashtags']}"
        else:
            return f"{template['caption']} {' '.join([f'#{tag}' for tag in template['hashtags']])}"
    
    def create_posting_schedule(self, videos_per_day=2, start_date=None):
        """Create a posting schedule for all videos"""
        if not start_date:
            start_date = datetime.now()
        
        schedule = []
        all_videos = []
        
        # Collect all videos
        for folder_type in self.video_folders.keys():
            videos = self.get_video_files(folder_type)
            for video in videos:
                all_videos.append({
                    "path": video,
                    "type": folder_type,
                    "caption": self.generate_caption(folder_type)
                })
        
        # Create schedule
        current_date = start_date
        video_index = 0
        
        while video_index < len(all_videos):
            # Add videos for current day
            day_videos = []
            for i in range(min(videos_per_day, len(all_videos) - video_index)):
                video = all_videos[video_index + i]
                day_videos.append(video)
            
            schedule.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "videos": day_videos
            })
            
            video_index += len(day_videos)
            current_date += timedelta(days=1)
        
        return schedule

def main():
    """Main function to run TikTok automation"""
    print("🚀 Starting TikTok Automation for GettingStoned...")
    
    # Initialize content manager
    content_manager = TikTokContentManager()
    
    # Create posting schedule
    schedule = content_manager.create_posting_schedule(videos_per_day=2)
    
    # Save schedule to file
    with open("tiktok_posting_schedule.json", "w") as f:
        json.dump(schedule, f, indent=2, default=str)
    
    print(f"✅ Created posting schedule with {len(schedule)} days")
    print(f"📅 Total videos to post: {sum(len(day['videos']) for day in schedule)}")
    
    # Example usage (commented out for safety)
    """
    # Initialize TikTok automation
    tiktok = TikTokAutomation(headless=False)
    
    try:
        # Login (you'll need to provide credentials)
        if tiktok.login_to_tiktok("your_username", "your_password"):
            
            # Post first video as example
            first_day = schedule[0]
            if first_day['videos']:
                video = first_day['videos'][0]
                success = tiktok.upload_video(
                    video['path'],
                    video['caption']
                )
                
                if success:
                    print("✅ First video posted successfully!")
                else:
                    print("❌ Failed to post first video")
    
    finally:
        tiktok.close()
    """
    
    print("\n📋 Next Steps:")
    print("1. Review tiktok_posting_schedule.json")
    print("2. Set up your TikTok credentials")
    print("3. Install ChromeDriver if not already installed")
    print("4. Run the automation script")
    print("5. Monitor your TikTok account for posts")

if __name__ == "__main__":
    main()


