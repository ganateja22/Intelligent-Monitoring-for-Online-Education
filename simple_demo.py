"""
Simple Demo of Student Attention Tracker
Run this to test the basic functionality without all features
"""

import cv2
import numpy as np
import time
from datetime import datetime

# Simple face detection using OpenCV's built-in detector
def simple_attention_demo():
    """Simplified attention tracking demo"""
    print("� AI-POWERED STUDENT ATTENTION TRACKER")
    print("=" * 60)
    print("📚 Smart Learning Focus Monitor for Online Education")
    print("💡 Real-time Computer Vision Attention Analysis")
    print("-" * 60)
    print("🎮 DEMO MODE: Basic face detection attention monitoring")
    print("📹 Controls: Press 'q' to quit, 's' to take screenshot")
    print("=" * 60)
    
    # Initialize camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Could not access camera")
        return
    
    # Load face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Tracking variables
    session_start = time.time()
    face_detected_time = 0
    total_frames = 0
    alert_threshold = 3  # seconds without face detection
    last_face_time = time.time()
    
    print("✅ Camera initialized successfully!")
    print("📹 Starting attention monitoring...")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error reading from camera")
            break
        
        # Flip frame for mirror effect
        frame = cv2.flip(frame, 1)
        total_frames += 1
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        current_time = time.time()
        session_duration = current_time - session_start
        
        # Check if face is detected
        face_detected = len(faces) > 0
        
        if face_detected:
            face_detected_time += 1/30  # Assuming 30 FPS
            last_face_time = current_time
            attention_status = "ATTENTIVE"
            status_color = (0, 255, 0)  # Green
            
            # Draw rectangle around face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "Face Detected", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        else:
            time_since_face = current_time - last_face_time
            if time_since_face > alert_threshold:
                attention_status = "NOT ATTENTIVE"
                status_color = (0, 0, 255)  # Red
                
                # Flash red border for alert
                if int(time_since_face * 2) % 2:  # Flash every 0.5 seconds
                    cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), 
                                 (0, 0, 255), 10)
            else:
                attention_status = "LOOKING AWAY"
                status_color = (0, 255, 255)  # Yellow
        
        # Calculate attention percentage
        attention_percentage = (face_detected_time / session_duration) * 100 if session_duration > 0 else 0
        
        # Draw status overlay
        cv2.rectangle(frame, (10, 10), (300, 120), (50, 50, 50), -1)
        
        # Status text
        cv2.putText(frame, f"Status: {attention_status}", (15, 35), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, status_color, 2)
        
        # Session info
        cv2.putText(frame, f"Session: {session_duration:.0f}s", (15, 55), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        cv2.putText(frame, f"Attention: {attention_percentage:.1f}%", (15, 75), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        cv2.putText(frame, f"Faces: {len(faces)}", (15, 95), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        
        # Instructions
        cv2.putText(frame, "Press 'q' to quit, 's' for screenshot", (10, frame.shape[0] - 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
        
        # Display frame
        cv2.imshow('Student Attention Tracker - Demo', frame)
        
        # Handle key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            # Save screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"attention_screenshot_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"📸 Screenshot saved: {filename}")
    
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    
    # Final session summary
    print("\n📊 Session Summary:")
    print("=" * 30)
    print(f"Total Duration: {session_duration:.1f} seconds")
    print(f"Attention Percentage: {attention_percentage:.1f}%")
    print(f"Face Detection Time: {face_detected_time:.1f} seconds")
    print(f"Total Frames: {total_frames}")
    
    if attention_percentage >= 80:
        grade = "Excellent! 🌟"
    elif attention_percentage >= 60:
        grade = "Good! 👍"
    elif attention_percentage >= 40:
        grade = "Fair 📚"
    else:
        grade = "Needs Improvement 📖"
    
    print(f"Grade: {grade}")

if __name__ == "__main__":
    try:
        simple_attention_demo()
    except KeyboardInterrupt:
        print("\n🛑 Demo stopped by user")
    except Exception as e:
        print(f"❌ Error running demo: {e}")
        print("💡 Make sure your camera is connected and not being used by another application")