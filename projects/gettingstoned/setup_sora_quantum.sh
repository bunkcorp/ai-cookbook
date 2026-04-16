#!/bin/bash

# Setup script for WASHBOARD QUANTUM: THE COHERENCE AWAKENING
echo "🎬 WASHBOARD QUANTUM: THE COHERENCE AWAKENING"
echo "Setting up Sora video generation for quantum physics visualization..."

# Check for OpenAI API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OpenAI API key not found!"
    echo "Please set your OpenAI API key:"
    echo "export OPENAI_API_KEY='your-api-key-here'"
    echo ""
    echo "You can get an API key from: https://platform.openai.com/api-keys"
    exit 1
fi

echo "✅ OpenAI API key found"

# Install required packages
echo "📦 Installing required packages..."
pip install openai requests

# Create output directory
echo "📁 Creating output directory..."
mkdir -p washboard_quantum_videos

# Check if Sora requests file exists
if [ ! -f "washboard_quantum_videos/washboard_quantum_sora_requests.json" ]; then
    echo "📝 Generating Sora video specifications..."
    python sora_washboard_quantum.py
fi

echo "✅ Setup complete!"
echo ""
echo "🚀 Ready to generate quantum physics videos with Sora!"
echo ""
echo "Next steps:"
echo "1. Review the generated prompts:"
echo "   cat washboard_quantum_videos/washboard_quantum_sora_requests.json"
echo ""
echo "2. Generate the videos:"
echo "   python generate_sora_videos.py"
echo ""
echo "3. The videos will be saved to: washboard_quantum_videos/"
echo ""
echo "⚠️  Note: Sora video generation can take several minutes per video"
echo "   and may incur significant API costs. Monitor your usage!"
echo ""
echo "🎬 This will create 5 video segments totaling 3:15 of quantum physics visualization:"
echo "   - Establishing shot (35s): Cosmic zoom to quantum junction"
echo "   - Act I (40s): Thermal chaos and quantum transition"
echo "   - Act II (40s): Microwave resonance and ladder climbing"
echo "   - Act III (40s): Macroscopic quantum tunneling"
echo "   - Act IV (40s): Bloch sphere and quantum gates"



