#!/usr/bin/env python3
"""
TikTok Analytics for GettingStoned Marketing
Track performance and optimize content strategy
"""

import json
import requests
from datetime import datetime, timedelta
from pathlib import Path

class TikTokAnalytics:
    def __init__(self):
        """Initialize TikTok analytics tracking"""
        self.metrics_file = "tiktok_analytics.json"
        self.posting_log_file = "tiktok_posting_log.json"
        self.analytics_data = self.load_analytics_data()
        
    def load_analytics_data(self):
        """Load existing analytics data"""
        try:
            with open(self.metrics_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "posts": [],
                "metrics": {
                    "total_views": 0,
                    "total_likes": 0,
                    "total_comments": 0,
                    "total_shares": 0,
                    "total_saves": 0
                },
                "performance_by_type": {},
                "best_posting_times": {},
                "top_hashtags": {},
                "engagement_rates": {}
            }
    
    def save_analytics_data(self):
        """Save analytics data to file"""
        with open(self.metrics_file, "w") as f:
            json.dump(self.analytics_data, f, indent=2)
    
    def track_post(self, video_path, video_type, caption, hashtags, posting_time):
        """Track a new post"""
        post_data = {
            "timestamp": datetime.now().isoformat(),
            "video_path": video_path,
            "video_type": video_type,
            "caption": caption,
            "hashtags": hashtags,
            "posting_time": posting_time,
            "metrics": {
                "views": 0,
                "likes": 0,
                "comments": 0,
                "shares": 0,
                "saves": 0,
                "engagement_rate": 0.0,
                "completion_rate": 0.0
            }
        }
        
        self.analytics_data["posts"].append(post_data)
        self.save_analytics_data()
        
        print(f"📊 Tracking post: {os.path.basename(video_path)}")
    
    def update_metrics(self, video_path, views=None, likes=None, comments=None, shares=None, saves=None):
        """Update metrics for a specific post"""
        for post in self.analytics_data["posts"]:
            if post["video_path"] == video_path:
                if views is not None:
                    post["metrics"]["views"] = views
                if likes is not None:
                    post["metrics"]["likes"] = likes
                if comments is not None:
                    post["metrics"]["comments"] = comments
                if shares is not None:
                    post["metrics"]["shares"] = shares
                if saves is not None:
                    post["metrics"]["saves"] = saves
                
                # Calculate engagement rate
                total_engagement = post["metrics"]["likes"] + post["metrics"]["comments"] + post["metrics"]["shares"] + post["metrics"]["saves"]
                if post["metrics"]["views"] > 0:
                    post["metrics"]["engagement_rate"] = (total_engagement / post["metrics"]["views"]) * 100
                
                break
        
        self.save_analytics_data()
    
    def get_performance_summary(self):
        """Get overall performance summary"""
        posts = self.analytics_data["posts"]
        
        if not posts:
            return {"message": "No posts tracked yet"}
        
        total_views = sum(post["metrics"]["views"] for post in posts)
        total_likes = sum(post["metrics"]["likes"] for post in posts)
        total_comments = sum(post["metrics"]["comments"] for post in posts)
        total_shares = sum(post["metrics"]["shares"] for post in posts)
        total_saves = sum(post["metrics"]["saves"] for post in posts)
        
        avg_engagement_rate = sum(post["metrics"]["engagement_rate"] for post in posts) / len(posts)
        
        return {
            "total_posts": len(posts),
            "total_views": total_views,
            "total_likes": total_likes,
            "total_comments": total_comments,
            "total_shares": total_shares,
            "total_saves": total_saves,
            "average_engagement_rate": round(avg_engagement_rate, 2),
            "average_views_per_post": round(total_views / len(posts), 2)
        }
    
    def get_performance_by_type(self):
        """Get performance breakdown by video type"""
        performance_by_type = {}
        
        for post in self.analytics_data["posts"]:
            video_type = post["video_type"]
            
            if video_type not in performance_by_type:
                performance_by_type[video_type] = {
                    "posts": 0,
                    "total_views": 0,
                    "total_likes": 0,
                    "total_comments": 0,
                    "total_shares": 0,
                    "total_saves": 0,
                    "avg_engagement_rate": 0.0
                }
            
            metrics = post["metrics"]
            performance_by_type[video_type]["posts"] += 1
            performance_by_type[video_type]["total_views"] += metrics["views"]
            performance_by_type[video_type]["total_likes"] += metrics["likes"]
            performance_by_type[video_type]["total_comments"] += metrics["comments"]
            performance_by_type[video_type]["total_shares"] += metrics["shares"]
            performance_by_type[video_type]["total_saves"] += metrics["saves"]
        
        # Calculate averages
        for video_type, data in performance_by_type.items():
            if data["posts"] > 0:
                total_engagement = data["total_likes"] + data["total_comments"] + data["total_shares"] + data["total_saves"]
                if data["total_views"] > 0:
                    data["avg_engagement_rate"] = round((total_engagement / data["total_views"]) * 100, 2)
                data["avg_views_per_post"] = round(data["total_views"] / data["posts"], 2)
        
        return performance_by_type
    
    def get_best_posting_times(self):
        """Analyze best posting times based on performance"""
        posting_times = {}
        
        for post in self.analytics_data["posts"]:
            posting_time = post["posting_time"]
            views = post["metrics"]["views"]
            
            if posting_time not in posting_times:
                posting_times[posting_time] = {"posts": 0, "total_views": 0}
            
            posting_times[posting_time]["posts"] += 1
            posting_times[posting_time]["total_views"] += views
        
        # Calculate average views per posting time
        for time_slot, data in posting_times.items():
            data["avg_views"] = round(data["total_views"] / data["posts"], 2)
        
        # Sort by average views
        sorted_times = sorted(posting_times.items(), key=lambda x: x[1]["avg_views"], reverse=True)
        
        return dict(sorted_times)
    
    def get_top_hashtags(self):
        """Analyze top performing hashtags"""
        hashtag_performance = {}
        
        for post in self.analytics_data["posts"]:
            hashtags = post["hashtags"]
            views = post["metrics"]["views"]
            
            for hashtag in hashtags:
                if hashtag not in hashtag_performance:
                    hashtag_performance[hashtag] = {"posts": 0, "total_views": 0}
                
                hashtag_performance[hashtag]["posts"] += 1
                hashtag_performance[hashtag]["total_views"] += views
        
        # Calculate average views per hashtag
        for hashtag, data in hashtag_performance.items():
            data["avg_views"] = round(data["total_views"] / data["posts"], 2)
        
        # Sort by average views
        sorted_hashtags = sorted(hashtag_performance.items(), key=lambda x: x[1]["avg_views"], reverse=True)
        
        return dict(sorted_hashtags)
    
    def generate_analytics_report(self):
        """Generate comprehensive analytics report"""
        print("📊 TikTok Analytics Report for GettingStoned")
        print("=" * 60)
        
        # Overall performance
        summary = self.get_performance_summary()
        print(f"\n📈 Overall Performance:")
        print(f"  Total Posts: {summary['total_posts']}")
        print(f"  Total Views: {summary['total_views']:,}")
        print(f"  Total Likes: {summary['total_likes']:,}")
        print(f"  Total Comments: {summary['total_comments']:,}")
        print(f"  Total Shares: {summary['total_shares']:,}")
        print(f"  Total Saves: {summary['total_saves']:,}")
        print(f"  Avg Engagement Rate: {summary['average_engagement_rate']}%")
        print(f"  Avg Views per Post: {summary['average_views_per_post']:,}")
        
        # Performance by type
        print(f"\n🎬 Performance by Video Type:")
        performance_by_type = self.get_performance_by_type()
        for video_type, data in performance_by_type.items():
            print(f"  {video_type}:")
            print(f"    Posts: {data['posts']}")
            print(f"    Total Views: {data['total_views']:,}")
            print(f"    Avg Views: {data['avg_views_per_post']:,}")
            print(f"    Engagement Rate: {data['avg_engagement_rate']}%")
        
        # Best posting times
        print(f"\n⏰ Best Posting Times:")
        best_times = self.get_best_posting_times()
        for time_slot, data in list(best_times.items())[:5]:
            print(f"  {time_slot}: {data['avg_views']:,} avg views ({data['posts']} posts)")
        
        # Top hashtags
        print(f"\n#️⃣ Top Performing Hashtags:")
        top_hashtags = self.get_top_hashtags()
        for hashtag, data in list(top_hashtags.items())[:10]:
            print(f"  #{hashtag}: {data['avg_views']:,} avg views ({data['posts']} posts)")
        
        # Save report
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "summary": summary,
            "performance_by_type": performance_by_type,
            "best_posting_times": best_times,
            "top_hashtags": top_hashtags
        }
        
        with open("tiktok_analytics_report.json", "w") as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n📁 Analytics report saved to: tiktok_analytics_report.json")
        
        return report_data
    
    def get_optimization_recommendations(self):
        """Get recommendations for optimizing content strategy"""
        recommendations = []
        
        # Analyze performance by type
        performance_by_type = self.get_performance_by_type()
        
        if performance_by_type:
            # Find best performing type
            best_type = max(performance_by_type.items(), key=lambda x: x[1]["avg_views_per_post"])
            recommendations.append(f"🎯 Focus on {best_type[0]} content (avg {best_type[1]['avg_views_per_post']:,} views)")
            
            # Find underperforming types
            worst_type = min(performance_by_type.items(), key=lambda x: x[1]["avg_views_per_post"])
            recommendations.append(f"⚠️ Improve {worst_type[0]} content (avg {worst_type[1]['avg_views_per_post']:,} views)")
        
        # Analyze posting times
        best_times = self.get_best_posting_times()
        if best_times:
            best_time = list(best_times.items())[0]
            recommendations.append(f"⏰ Post more at {best_time[0]} (avg {best_time[1]['avg_views']:,} views)")
        
        # Analyze hashtags
        top_hashtags = self.get_top_hashtags()
        if top_hashtags:
            top_hashtag = list(top_hashtags.items())[0]
            recommendations.append(f"#️⃣ Use #{top_hashtag[0]} more often (avg {top_hashtag[1]['avg_views']:,} views)")
        
        return recommendations

def main():
    """Main analytics function"""
    print("📊 TikTok Analytics for GettingStoned")
    print("=" * 50)
    
    analytics = TikTokAnalytics()
    
    # Generate report
    report = analytics.generate_analytics_report()
    
    # Get recommendations
    recommendations = analytics.get_optimization_recommendations()
    
    if recommendations:
        print(f"\n💡 Optimization Recommendations:")
        for rec in recommendations:
            print(f"  {rec}")
    
    print(f"\n📋 Next Steps:")
    print("1. Review the analytics report")
    print("2. Implement optimization recommendations")
    print("3. Adjust your content strategy")
    print("4. Continue tracking performance")

if __name__ == "__main__":
    main()




