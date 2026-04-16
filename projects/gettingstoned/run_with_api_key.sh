#!/bin/bash
# Script to run GettingStoned video generation with API key

echo "🔑 GettingStoned Video Generation with API Key"
echo "=============================================="

# Check if API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY environment variable not set"
    echo ""
    echo "To set your API key, run one of these commands:"
    echo ""
    echo "Option 1 - Set for current session:"
    echo "export OPENAI_API_KEY='your-api-key-here'"
    echo ""
    echo "Option 2 - Add to your shell profile:"
    echo "echo 'export OPENAI_API_KEY=\"your-api-key-here\"' >> ~/.zshrc"
    echo "source ~/.zshrc"
    echo ""
    echo "Option 3 - Create .env file:"
    echo "echo 'OPENAI_API_KEY=your-api-key-here' > .env"
    echo ""
    echo "Then run this script again"
    exit 1
fi

echo "✅ API Key found: ${OPENAI_API_KEY:0:10}..."
echo ""

# Function to run video generation
run_video_generation() {
    local script_name=$1
    local description=$2
    
    echo "🎬 $description"
    echo "Running: $script_name"
    echo "----------------------------------------"
    
    if python "$script_name"; then
        echo "✅ $description completed successfully"
        return 0
    else
        echo "❌ $description failed"
        return 1
    fi
}

# Main menu
echo "What would you like to do?"
echo "1. Generate all screenshot-enhanced videos"
echo "2. Generate Ten Non-Virtues series"
echo "3. Generate call-to-action videos"
echo "4. Generate all videos"
echo "5. Check current video status"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        run_video_generation "sora_enhanced_with_screenshots.py" "Screenshot-Enhanced Videos"
        ;;
    2)
        run_video_generation "sora_ten_non_virtues_videos.py" "Ten Non-Virtues Series"
        ;;
    3)
        run_video_generation "sora_marketing_with_cta.py" "Call-to-Action Videos"
        ;;
    4)
        echo "🎬 Generating all videos..."
        run_video_generation "sora_enhanced_with_screenshots.py" "Screenshot-Enhanced Videos"
        run_video_generation "sora_ten_non_virtues_videos.py" "Ten Non-Virtues Series"
        run_video_generation "sora_marketing_with_cta.py" "Call-to-Action Videos"
        ;;
    5)
        echo "📊 Current Video Status:"
        echo "Screenshot videos: $(ls screenshot_enhanced_videos/*.mp4 2>/dev/null | wc -l)"
        echo "Ten virtues videos: $(ls ten_non_virtues_videos/*.mp4 2>/dev/null | wc -l)"
        echo "CTA videos: $(ls cta_videos/*.mp4 2>/dev/null | wc -l)"
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "🎉 Video generation complete!"





