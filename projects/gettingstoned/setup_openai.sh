#!/bin/bash

echo "🎬 GettingStoned Sora Video Generator Setup"
echo "=========================================="

# Check if OpenAI API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY not found"
    echo ""
    echo "Please set your OpenAI API key:"
    echo "1. Get your API key from: https://platform.openai.com/api-keys"
    echo "2. Run: export OPENAI_API_KEY='your-api-key-here'"
    echo "3. Or add it to your ~/.zshrc file for persistence"
    echo ""
    echo "Example:"
    echo "export OPENAI_API_KEY='sk-proj-...'"
    echo ""
    echo "Then run this script again to continue setup."
    exit 1
else
    echo "✅ OPENAI_API_KEY is set"
fi

# Install required packages
echo "📦 Installing required packages..."
pip install openai pydantic requests pillow

# Create output directories
echo "📁 Creating output directories..."
mkdir -p ./screenshot_enhanced_videos
mkdir -p ./marketing_videos
mkdir -p ./manifesto_videos
mkdir -p ./ecosystem_videos
mkdir -p ./emptiness_analysis_videos
mkdir -p ./ten_non_virtues_videos

echo "✅ Setup complete!"
echo ""
echo "🚀 Ready to generate videos!"
echo ""
echo "Test with a single video:"
echo "python sora_enhanced_with_screenshots.py single app_interface_hero"
echo ""
echo "Generate all screenshot-enhanced videos:"
echo "python sora_enhanced_with_screenshots.py all"
echo ""
echo "Generate all video types:"
echo "python sora_marketing_generator.py all"
echo "python sora_manifesto_videos.py all"
echo "python sora_enhanced_ecosystem_videos.py all"
echo "python sora_emptiness_analysis_videos.py all"
echo "python sora_ten_non_virtues_videos.py all"
