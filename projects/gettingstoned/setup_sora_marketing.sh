#!/bin/bash

# Setup script for GettingStoned Sora Marketing Videos
echo "🎬 Setting up Sora Marketing Video Generator for GettingStoned"
echo "=============================================================="

# Check if OpenAI API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY environment variable not set"
    echo "Please set your OpenAI API key:"
    echo "export OPENAI_API_KEY='your-api-key-here'"
    exit 1
fi

# Create marketing videos directory
mkdir -p marketing_videos
echo "📁 Created marketing_videos directory"

# Make the script executable
chmod +x sora_marketing_generator.py
echo "🔧 Made sora_marketing_generator.py executable"

# Install required dependencies
echo "📦 Installing dependencies..."
pip install openai pydantic requests pillow

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎬 Usage Examples:"
echo "  python sora_marketing_generator.py list                    # List all video prompts"
echo "  python sora_marketing_generator.py single hero_stress_to_calm  # Create hero video"
echo "  python sora_marketing_generator.py all                     # Create all marketing videos"
echo ""
echo "📋 Available video types:"
echo "  - hero_stress_to_calm: Main hero video showing transformation"
echo "  - app_discovery: App discovery moment"
echo "  - mantra_practice: Mantra recognition demo"
echo "  - prostration_detection: Prostration detection demo"
echo "  - karma_visualization: Karma analysis visualization"
echo "  - muse_eeg_integration: Muse EEG integration"
echo "  - urban_professional: Professional testimonial"
echo "  - spiritual_journey: Complete user journey"
echo ""
echo "💡 Start with: python sora_marketing_generator.py single hero_stress_to_calm"
