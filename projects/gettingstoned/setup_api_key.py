#!/usr/bin/env python3
"""
Setup OpenAI API Key for GettingStoned Video Generation
"""

import os
import sys

def setup_api_key():
    """Setup OpenAI API key"""
    print("🔑 Setting up OpenAI API Key for GettingStoned Video Generation")
    print("=" * 60)
    
    # Check if API key is already set
    current_key = os.getenv('OPENAI_API_KEY')
    if current_key:
        print(f"✅ API Key already set: {current_key[:10]}...")
        return True
    
    print("\n📋 To get your OpenAI API key:")
    print("1. Go to https://platform.openai.com/account/api-keys")
    print("2. Click 'Create new secret key'")
    print("3. Copy the key (starts with 'sk-')")
    print("4. Paste it below")
    
    api_key = input("\n🔑 Enter your OpenAI API key: ").strip()
    
    if not api_key.startswith('sk-'):
        print("❌ Invalid API key format. Should start with 'sk-'")
        return False
    
    # Set the environment variable
    os.environ['OPENAI_API_KEY'] = api_key
    
    # Save to .env file for persistence
    with open('.env', 'w') as f:
        f.write(f"OPENAI_API_KEY={api_key}\n")
    
    print("✅ API key set successfully!")
    print("✅ Saved to .env file for future use")
    
    return True

def test_api_key():
    """Test the API key"""
    try:
        from openai import OpenAI
        client = OpenAI()
        
        # Test with a simple request
        response = client.models.list()
        print("✅ API key is working!")
        return True
    except Exception as e:
        print(f"❌ API key test failed: {e}")
        return False

def main():
    """Main setup function"""
    if setup_api_key():
        print("\n🧪 Testing API key...")
        if test_api_key():
            print("\n🎉 Setup complete! You can now generate videos.")
            print("\n🚀 Next steps:")
            print("1. Run: python sora_enhanced_with_screenshots.py all")
            print("2. Run: python sora_ten_non_virtues_videos.py")
            print("3. Run: python sora_marketing_with_cta.py")
        else:
            print("\n❌ API key test failed. Please check your key.")
    else:
        print("\n❌ Setup failed. Please try again.")

if __name__ == "__main__":
    main()





