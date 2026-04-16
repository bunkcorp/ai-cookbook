#!/bin/bash

# TikTok Automation Setup Script for GettingStoned
echo "🚀 Setting up TikTok automation for GettingStoned..."

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r tiktok_requirements.txt

# Install ChromeDriver
echo "🌐 Installing ChromeDriver..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install chromedriver
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/LATEST_RELEASE/chromedriver_linux64.zip
    unzip /tmp/chromedriver.zip -d /tmp/
    sudo mv /tmp/chromedriver /usr/local/bin/
    sudo chmod +x /usr/local/bin/chromedriver
else
    echo "❌ Unsupported OS. Please install ChromeDriver manually."
    exit 1
fi

# Create environment file
echo "🔐 Creating environment file..."
cat > .env << EOF
# TikTok Credentials
TIKTOK_USERNAME=your_username_here
TIKTOK_PASSWORD=your_password_here

# Posting Settings
POSTS_PER_DAY=2
HEADLESS_MODE=true
SCHEDULE_DAYS=30
EOF

echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env file with your TikTok credentials"
echo "2. Run: python tiktok_scheduler.py"
echo "3. Choose option 1 to create schedule first"
echo "4. Review manual_tiktok_schedule.json"
echo "5. Run with option 2 to execute posts"
echo ""
echo "⚠️  Important:"
echo "- Make sure your TikTok account is set up for business use"
echo "- Test with a few videos first before full automation"
echo "- Keep your credentials secure"




