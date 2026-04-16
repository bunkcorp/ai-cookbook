#!/bin/bash

# WASHBOARD QUANTUM: THE COHERENCE AWAKENING - Video Generation Script
echo "🎬 WASHBOARD QUANTUM: THE COHERENCE AWAKENING"
echo "Quantum Physics Visualization with Sora"
echo "=============================================="

# Check if API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY not found!"
    echo ""
    echo "Please set your API key first:"
    echo "export OPENAI_API_KEY='your-api-key-here'"
    echo ""
    echo "You can get your API key from: https://platform.openai.com/api-keys"
    echo ""
    echo "Then run this script again:"
    echo "./run_washboard_quantum.sh"
    exit 1
fi

echo "✅ API Key found: ${OPENAI_API_KEY:0:10}..."
echo ""

# Create output directory
mkdir -p washboard_quantum_videos

# Generate the Sora video specifications first
echo "📝 Generating Sora video specifications..."
python sora_washboard_quantum.py

# Generate the videos
echo "🎬 Generating quantum physics videos with Sora..."
python generate_sora_videos.py

echo ""
echo "🎉 WASHBOARD QUANTUM video generation complete!"
echo "📁 Videos saved to: washboard_quantum_videos/"
echo "📋 Playlist: washboard_quantum_videos/washboard_quantum_playlist.txt"



