# 🎬 TikTok Automation for GettingStoned

Complete TikTok posting automation system for your GettingStoned marketing campaign.

## 🚀 Quick Start

### 1. Setup
```bash
# Run the setup script
./setup_tiktok.sh

# Or manually install dependencies
pip install -r tiktok_requirements.txt
brew install chromedriver  # macOS
```

### 2. Configure Credentials
Edit the `.env` file with your TikTok credentials:
```
TIKTOK_USERNAME=your_username_here
TIKTOK_PASSWORD=your_password_here
```

### 3. Test the System
```bash
python test_tiktok_system.py
```

### 4. Create Posting Schedule
```bash
python tiktok_scheduler.py
# Choose option 1 to create schedule
```

### 5. Execute Posts
```bash
python tiktok_scheduler.py
# Choose option 2 to execute posts
```

## 📁 Files Overview

| File | Purpose |
|------|---------|
| `tiktok_automation.py` | Core automation using Selenium |
| `tiktok_scheduler.py` | Scheduling and posting system |
| `tiktok_config.py` | Content templates and optimization |
| `tiktok_analytics.py` | Performance tracking and analytics |
| `test_tiktok_system.py` | System testing and validation |
| `setup_tiktok.sh` | Automated setup script |

## 🎯 Features

### ✅ Automated Posting
- Browser automation using Selenium
- Scheduled posting with optimal timing
- Content optimization for TikTok
- Hashtag strategy and captions

### ✅ Content Management
- Multiple video types support
- Optimized captions and hooks
- Hashtag optimization
- Content scheduling

### ✅ Analytics & Tracking
- Performance metrics tracking
- Engagement rate analysis
- Best posting time optimization
- Hashtag performance analysis

### ✅ Safety Features
- Headless mode option
- Error handling and recovery
- Posting logs and audit trail
- Rate limiting and delays

## 📊 Content Strategy

### Video Types
- **App Launch**: Introduction and features
- **Stone Logging**: Karma tracking demo
- **Ten Non-Virtues**: Educational content
- **Karma Visualization**: Data visualization
- **Meditation Tracking**: Practice tracking
- **Feature Showcase**: App capabilities

### Posting Schedule
- **Frequency**: 2-3 posts per day
- **Optimal Times**: 10 AM, 2 PM, 8 PM
- **Content Mix**: 40% educational, 30% features, 20% inspirational, 10% CTA

### Hashtag Strategy
- **Primary**: #GettingStoned, #SpiritualTech, #Meditation
- **Secondary**: #Mindfulness, #Karma, #Buddhism
- **Trending**: #AI, #TechForGood, #FYP

## 🔧 Configuration

### Environment Variables
```bash
TIKTOK_USERNAME=your_username
TIKTOK_PASSWORD=your_password
POSTS_PER_DAY=2
HEADLESS_MODE=true
SCHEDULE_DAYS=30
```

### Content Templates
Each video type has optimized:
- Hooks for engagement
- Captions for clarity
- Hashtags for reach
- Call-to-actions for conversion

## 📈 Analytics

### Tracked Metrics
- Views, likes, comments, shares, saves
- Engagement rates
- Completion rates
- Performance by video type
- Best posting times
- Top performing hashtags

### Reports Generated
- `tiktok_analytics_report.json` - Comprehensive analytics
- `tiktok_posting_log.json` - Posting history
- `tiktok_test_report.json` - System test results

## ⚠️ Important Notes

### TikTok Limitations
- No official API for video uploads
- Browser automation required
- Rate limiting applies
- Account safety considerations

### Best Practices
1. **Test First**: Always test with a few videos before full automation
2. **Monitor Performance**: Check analytics regularly
3. **Vary Content**: Don't post the same type repeatedly
4. **Engage**: Respond to comments and engage with audience
5. **Comply**: Follow TikTok's community guidelines

### Safety Measures
- Headless mode for production
- Delays between posts
- Error handling and recovery
- Logging and audit trails
- Rate limiting compliance

## 🚨 Troubleshooting

### Common Issues
1. **ChromeDriver not found**: Install with `brew install chromedriver`
2. **Login failed**: Check credentials and account status
3. **Upload timeout**: Increase wait times in automation
4. **Rate limiting**: Reduce posting frequency

### Debug Mode
```bash
# Run with visible browser for debugging
python tiktok_scheduler.py
# Set HEADLESS_MODE=false in .env
```

## 📋 Usage Examples

### Create Schedule Only
```bash
python tiktok_scheduler.py
# Choose option 1
# Review manual_tiktok_schedule.json
```

### Execute Manual Schedule
```bash
python tiktok_scheduler.py
# Choose option 2
# Enter credentials when prompted
```

### Run Continuous Scheduler
```bash
python tiktok_scheduler.py
# Choose option 3
# Runs continuously with scheduled posts
```

### Generate Analytics Report
```bash
python tiktok_analytics.py
# Generates comprehensive performance report
```

## 🎯 Success Metrics

### Target Goals
- **Views**: 10K+ per video
- **Engagement**: 5%+ rate
- **Completion**: 80%+ rate
- **Downloads**: 2%+ conversion

### Optimization
- A/B test different captions
- Experiment with posting times
- Test various hashtag combinations
- Monitor and adjust strategy

## 🔄 Workflow

1. **Setup**: Install dependencies and configure credentials
2. **Test**: Run system tests to verify functionality
3. **Schedule**: Create posting schedule for your videos
4. **Execute**: Run automated posting
5. **Monitor**: Track performance and analytics
6. **Optimize**: Adjust strategy based on results

## 📞 Support

For issues or questions:
1. Check the test report: `python test_tiktok_system.py`
2. Review logs: `tiktok_posting_log.json`
3. Check analytics: `python tiktok_analytics.py`
4. Verify system requirements

---

*This system automates your TikTok posting while maintaining compliance with platform guidelines and optimizing for engagement.*




