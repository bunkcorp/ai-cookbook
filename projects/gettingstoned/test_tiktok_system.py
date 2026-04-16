#!/usr/bin/env python3
"""
Test TikTok System for GettingStoned
Verifies all components work correctly
"""

import os
import json
from pathlib import Path
from tiktok_config import get_posting_schedule, get_optimized_caption, CONTENT_TEMPLATES
from tiktok_automation import TikTokContentManager

def test_content_manager():
    """Test TikTokContentManager functionality"""
    print("🧪 Testing TikTokContentManager...")
    
    try:
        manager = TikTokContentManager()
        
        # Test getting video files
        for folder_type in manager.video_folders.keys():
            videos = manager.get_video_files(folder_type)
            print(f"  📁 {folder_type}: {len(videos)} videos found")
            
            if videos:
                print(f"    📹 Sample: {os.path.basename(videos[0])}")
        
        # Test caption generation
        for video_type in CONTENT_TEMPLATES.keys():
            caption = manager.generate_caption(video_type)
            print(f"  📝 {video_type}: {len(caption)} chars")
        
        print("✅ TikTokContentManager test passed")
        return True
        
    except Exception as e:
        print(f"❌ TikTokContentManager test failed: {e}")
        return False

def test_content_templates():
    """Test content template generation"""
    print("🧪 Testing content templates...")
    
    try:
        for video_type, template in CONTENT_TEMPLATES.items():
            caption = get_optimized_caption(video_type)
            
            # Check caption length (TikTok limit is 2200 chars)
            if len(caption) > 2200:
                print(f"  ⚠️ {video_type}: Caption too long ({len(caption)} chars)")
            else:
                print(f"  ✅ {video_type}: Caption length OK ({len(caption)} chars)")
            
            # Check hashtag count (optimal is 3-5)
            hashtag_count = len(template['hashtags'])
            if hashtag_count > 10:
                print(f"  ⚠️ {video_type}: Too many hashtags ({hashtag_count})")
            else:
                print(f"  ✅ {video_type}: Hashtag count OK ({hashtag_count})")
        
        print("✅ Content templates test passed")
        return True
        
    except Exception as e:
        print(f"❌ Content templates test failed: {e}")
        return False

def test_posting_schedule():
    """Test posting schedule generation"""
    print("🧪 Testing posting schedule...")
    
    try:
        schedule = get_posting_schedule(days=7, videos_per_day=2)
        
        print(f"  📅 Generated {len(schedule)} days of content")
        
        total_videos = sum(len(day['videos']) for day in schedule)
        print(f"  📹 Total videos: {total_videos}")
        
        # Check video type distribution
        video_types = {}
        for day in schedule:
            for video in day['videos']:
                video_type = video['type']
                video_types[video_type] = video_types.get(video_type, 0) + 1
        
        print("  📊 Video type distribution:")
        for video_type, count in video_types.items():
            print(f"    {video_type}: {count} videos")
        
        print("✅ Posting schedule test passed")
        return True
        
    except Exception as e:
        print(f"❌ Posting schedule test failed: {e}")
        return False

def test_video_files():
    """Test video file availability"""
    print("🧪 Testing video file availability...")
    
    try:
        manager = TikTokContentManager()
        total_videos = 0
        
        for folder_type in manager.video_folders.keys():
            videos = manager.get_video_files(folder_type)
            total_videos += len(videos)
            
            if videos:
                print(f"  ✅ {folder_type}: {len(videos)} videos available")
                
                # Check file sizes
                for video in videos[:3]:  # Check first 3 videos
                    size_mb = os.path.getsize(video) / (1024 * 1024)
                    print(f"    📹 {os.path.basename(video)}: {size_mb:.1f} MB")
            else:
                print(f"  ⚠️ {folder_type}: No videos found")
        
        print(f"  📊 Total videos available: {total_videos}")
        
        if total_videos > 0:
            print("✅ Video files test passed")
            return True
        else:
            print("❌ No video files found")
            return False
        
    except Exception as e:
        print(f"❌ Video files test failed: {e}")
        return False

def test_system_requirements():
    """Test system requirements"""
    print("🧪 Testing system requirements...")
    
    try:
        # Check Python packages
        required_packages = [
            'selenium',
            'schedule', 
            'requests',
            'pathlib'
        ]
        
        missing_packages = []
        for package in required_packages:
            try:
                __import__(package)
                print(f"  ✅ {package}: Available")
            except ImportError:
                missing_packages.append(package)
                print(f"  ❌ {package}: Missing")
        
        if missing_packages:
            print(f"  ⚠️ Missing packages: {', '.join(missing_packages)}")
            print("  💡 Run: pip install -r tiktok_requirements.txt")
        
        # Check ChromeDriver
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            driver = webdriver.Chrome(options=chrome_options)
            driver.quit()
            print("  ✅ ChromeDriver: Available")
        except Exception as e:
            print(f"  ❌ ChromeDriver: {e}")
            print("  💡 Install ChromeDriver: brew install chromedriver")
        
        print("✅ System requirements test completed")
        return len(missing_packages) == 0
        
    except Exception as e:
        print(f"❌ System requirements test failed: {e}")
        return False

def generate_test_report():
    """Generate a comprehensive test report"""
    print("📊 Generating TikTok System Test Report...")
    print("=" * 60)
    
    tests = [
        ("Content Manager", test_content_manager),
        ("Content Templates", test_content_templates),
        ("Posting Schedule", test_posting_schedule),
        ("Video Files", test_video_files),
        ("System Requirements", test_system_requirements)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n🧪 Running {test_name} test...")
        results[test_name] = test_func()
    
    # Generate report
    print("\n" + "=" * 60)
    print("📋 TEST REPORT")
    print("=" * 60)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:20} {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! System is ready for TikTok automation.")
    else:
        print("⚠️ Some tests failed. Please address the issues before proceeding.")
    
    # Save report to file
    report_data = {
        "timestamp": str(datetime.now()),
        "results": results,
        "summary": {
            "passed": passed,
            "total": total,
            "success_rate": f"{(passed/total)*100:.1f}%"
        }
    }
    
    with open("tiktok_test_report.json", "w") as f:
        json.dump(report_data, f, indent=2)
    
    print(f"\n📁 Test report saved to: tiktok_test_report.json")
    
    return passed == total

def main():
    """Main test function"""
    print("🧪 TikTok System Test Suite for GettingStoned")
    print("=" * 60)
    
    # Import datetime for report
    from datetime import datetime
    
    # Run all tests
    success = generate_test_report()
    
    if success:
        print("\n🚀 System is ready for TikTok automation!")
        print("\nNext steps:")
        print("1. Run: python tiktok_scheduler.py")
        print("2. Choose option 1 to create schedule")
        print("3. Review manual_tiktok_schedule.json")
        print("4. Set up TikTok credentials")
        print("5. Execute automated posting")
    else:
        print("\n⚠️ Please fix the issues above before proceeding.")
        print("\nCommon fixes:")
        print("- Install missing packages: pip install -r tiktok_requirements.txt")
        print("- Install ChromeDriver: brew install chromedriver")
        print("- Ensure video files are in the correct folders")

if __name__ == "__main__":
    main()




