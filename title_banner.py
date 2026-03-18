"""
Professional Title Banner for AI-Powered Student Attention Tracker
"""

def display_main_title():
    """Display the main application title banner"""
    print()
    print("=" * 80)
    print("🎯 AI-POWERED STUDENT ATTENTION TRACKER".center(80))
    print("🧠 Smart Learning Focus Monitor for Online Education".center(80))
    print("💡 Real-time Computer Vision Attention Analysis System".center(80))
    print("=" * 80)
    print()

def display_version_info():
    """Display version and feature information"""
    print("📋 VERSION INFO:")
    print("   🚀 Version: 1.0 - Production Ready")
    print("   🎯 Features: Face Detection, Eye Tracking, Analytics")
    print("   🔧 Tech Stack: OpenCV, SQLite, Machine Learning")
    print("   📊 Output: Real-time Scoring, Graphs, Reports")
    print("-" * 80)

def display_usage_options():
    """Display available usage options"""
    print("🎮 AVAILABLE MODES:")
    print("   1️⃣  BASIC MODE    - Simple face detection tracking")
    print("   2️⃣  ENHANCED MODE - Full analytics with database logging")
    print("   3️⃣  ANALYTICS     - Generate comprehensive reports")
    print("-" * 80)
    
def display_controls():
    """Display control instructions"""
    print("🎮 CONTROLS DURING TRACKING:")
    print("   ⌨️  'Q' - Quit and generate final report")
    print("   📊 'R' - Generate session performance report")
    print("   📈 'G' - Show comprehensive analytics graphs")
    print("   📸 'S' - Take screenshot with overlay")
    print("=" * 80)

def display_footer():
    """Display footer with credits"""
    print()
    print("-" * 80)
    print("🎓 Designed for Students, Educators, and Researchers".center(80))
    print("🌟 Improve Online Learning Focus and Engagement".center(80))
    print("✨ AI-Powered Education Technology for Better Outcomes".center(80))
    print("-" * 80)
    print()

def show_complete_banner():
    """Show complete professional banner"""
    display_main_title()
    display_version_info()
    display_usage_options()
    display_controls()
    display_footer()

if __name__ == "__main__":
    show_complete_banner()