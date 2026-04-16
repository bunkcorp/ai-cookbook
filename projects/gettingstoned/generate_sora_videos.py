#!/usr/bin/env python3
"""
Generate Sora Videos for WASHBOARD QUANTUM: THE COHERENCE AWAKENING
Uses OpenAI's Sora API to create quantum physics visualization videos
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path
import openai

class SoraVideoGenerator:
    def __init__(self, api_key=None):
        """Initialize Sora video generator"""
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key required. Set OPENAI_API_KEY environment variable.")
        
        openai.api_key = self.api_key
        self.client = openai.OpenAI(api_key=self.api_key)
        
        self.output_dir = Path("washboard_quantum_videos")
        self.output_dir.mkdir(exist_ok=True)
        
    def load_sora_requests(self):
        """Load Sora video generation requests"""
        requests_file = self.output_dir / "washboard_quantum_sora_requests.json"
        
        with open(requests_file, 'r') as f:
            data = json.load(f)
        
        return data['requests']
    
    def generate_video(self, request, max_retries=3):
        """Generate a single Sora video"""
        print(f"🎬 Generating: {request['title']}")
        print(f"   Duration: {request['duration']}")
        print(f"   Style: {request['style']}")
        print(f"   Prompt length: {len(request['prompt'])} characters")
        
        for attempt in range(max_retries):
            try:
                print(f"   Attempt {attempt + 1}/{max_retries}...")
                
                # Generate video using Sora API
                response = self.client.videos.generate(
                    model="sora-1.0",
                    prompt=request['prompt'],
                    duration=request['duration'],
                    style=request['style'],
                    quality="hd",
                    aspect_ratio="21:9"  # CinemaScope
                )
                
                # Save video
                video_url = response.data[0].url
                output_file = self.output_dir / request['output_file']
                
                # Download video (you'll need to implement this)
                self.download_video(video_url, output_file)
                
                print(f"   ✅ Success! Saved to: {output_file}")
                return True
                
            except Exception as e:
                print(f"   ❌ Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    print(f"   ⏳ Waiting 30 seconds before retry...")
                    time.sleep(30)
                else:
                    print(f"   💥 All attempts failed for {request['title']}")
                    return False
    
    def download_video(self, url, output_path):
        """Download video from URL to local file"""
        import requests
        
        print(f"   📥 Downloading video from {url}...")
        
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"   💾 Video saved to: {output_path}")
    
    def generate_all_videos(self):
        """Generate all Sora videos for the quantum simulation"""
        print("🚀 WASHBOARD QUANTUM: THE COHERENCE AWAKENING")
        print("=" * 60)
        print("Generating quantum physics visualization videos with Sora...")
        
        # Load requests
        requests = self.load_sora_requests()
        
        print(f"\n📋 Found {len(requests)} video segments to generate:")
        for i, request in enumerate(requests, 1):
            print(f"  {i}. {request['title']} ({request['duration']})")
        
        # Generate each video
        results = []
        start_time = datetime.now()
        
        for i, request in enumerate(requests, 1):
            print(f"\n🎬 [{i}/{len(requests)}] Generating: {request['title']}")
            print("-" * 50)
            
            success = self.generate_video(request)
            results.append({
                "title": request['title'],
                "success": success,
                "timestamp": datetime.now().isoformat()
            })
            
            if success:
                print(f"✅ {request['title']} completed successfully")
            else:
                print(f"❌ {request['title']} failed")
            
            # Wait between requests to avoid rate limiting
            if i < len(requests):
                print("⏳ Waiting 60 seconds before next video...")
                time.sleep(60)
        
        # Generate summary
        end_time = datetime.now()
        duration = end_time - start_time
        
        successful = sum(1 for r in results if r['success'])
        failed = len(results) - successful
        
        print(f"\n📊 GENERATION SUMMARY:")
        print(f"  Total videos: {len(results)}")
        print(f"  Successful: {successful}")
        print(f"  Failed: {failed}")
        print(f"  Total time: {duration}")
        print(f"  Average per video: {duration / len(results)}")
        
        # Save results
        results_file = self.output_dir / "generation_results.json"
        with open(results_file, 'w') as f:
            json.dump({
                "summary": {
                    "total_videos": len(results),
                    "successful": successful,
                    "failed": failed,
                    "duration": str(duration),
                    "start_time": start_time.isoformat(),
                    "end_time": end_time.isoformat()
                },
                "results": results
            }, f, indent=2)
        
        print(f"\n📁 Results saved to: {results_file}")
        
        if successful > 0:
            print(f"\n🎉 SUCCESS! Generated {successful} quantum physics videos")
            print(f"📁 Check the {self.output_dir} directory for your videos")
        
        if failed > 0:
            print(f"\n⚠️ {failed} videos failed to generate")
            print("Check the error messages above for details")
        
        return results
    
    def create_video_playlist(self):
        """Create a playlist file for the generated videos"""
        playlist_file = self.output_dir / "washboard_quantum_playlist.txt"
        
        with open(playlist_file, 'w') as f:
            f.write("WASHBOARD QUANTUM: THE COHERENCE AWAKENING - Video Playlist\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("Play in this order for the complete 3:15 experience:\n\n")
            
            f.write("1. ESTABLISHING SHOT (35s)\n")
            f.write("   File: washboard_quantum_establishing_shot.mp4\n")
            f.write("   Description: Cosmic zoom from universe to quantum junction\n\n")
            
            f.write("2. ACT I - THERMAL PRISON (40s)\n")
            f.write("   File: washboard_quantum_act_i_thermal.mp4\n")
            f.write("   Description: Thermal chaos and quantum regime transition\n\n")
            
            f.write("3. ACT II - RESONANT AWAKENING (40s)\n")
            f.write("   File: washboard_quantum_act_ii_resonant.mp4\n")
            f.write("   Description: Microwave resonance and quantum ladder climbing\n\n")
            
            f.write("4. ACT III - QUANTUM TUNNEL (40s)\n")
            f.write("   File: washboard_quantum_act_iii_quantum.mp4\n")
            f.write("   Description: Macroscopic quantum tunneling through barrier\n\n")
            
            f.write("5. ACT IV - COHERENT GODHOOD (40s)\n")
            f.write("   File: washboard_quantum_act_iv_coherent.mp4\n")
            f.write("   Description: Bloch sphere and quantum gate operations\n\n")
            
            f.write("Total Duration: 195 seconds (3:15)\n")
            f.write("Aspect Ratio: 21:9 CinemaScope\n")
            f.write("Quality: HD (8K master, 4K delivery)\n")
            f.write("Style: IMAX cosmic gravity meets quantum physics\n\n")
            
            f.write("For best experience:\n")
            f.write("- Play on large screen or VR headset\n")
            f.write("- Use high-quality audio system\n")
            f.write("- Watch in dark environment\n")
            f.write("- Consider physics consultant for educational use\n")
        
        print(f"📋 Playlist created: {playlist_file}")

def main():
    """Main function to generate Sora videos"""
    print("🎬 WASHBOARD QUANTUM: THE COHERENCE AWAKENING")
    print("Sora Video Generation for Quantum Physics Visualization")
    print("=" * 60)
    
    # Check for API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OpenAI API key not found!")
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return
    
    try:
        # Initialize generator
        generator = SoraVideoGenerator(api_key)
        
        # Generate all videos
        results = generator.generate_all_videos()
        
        # Create playlist
        generator.create_video_playlist()
        
        print(f"\n🎉 QUANTUM PHYSICS VISUALIZATION COMPLETE!")
        print(f"📁 Videos saved to: {generator.output_dir}")
        print(f"📋 Playlist: {generator.output_dir}/washboard_quantum_playlist.txt")
        
        print(f"\n🚀 NEXT STEPS:")
        print(f"1. Review generated videos")
        print(f"2. Combine into final 3:15 video")
        print(f"3. Add quantum physics audio track")
        print(f"4. Export in 8K HDR for maximum impact")
        print(f"5. Share with physics community!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your API key and try again")

if __name__ == "__main__":
    main()



