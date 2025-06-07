# -HandSwipe-Game-Controller🎮🖐️
Control simple games using real-time hand gestures via webcam using MediaPipe + OpenCV.

Control your games using just hand gestures with this lightweight, real-time Hand Gesture Game Controller built using OpenCV, MediaPipe, and PyAutoGUI. No need for a joystick — your index finger is the controller!

---

## 📽️ Demo

![demo](https://user-images.githubusercontent.com/your-gif-or-screenshot.gif)
> *(Add your own screen recording here of the controller in action!)*

---

## 🚀 Features

- 👆 Detects real-time hand gestures using your webcam
- 👉 Swipe gestures (Up, Down, Left, Right) mapped to arrow keys
- 🕹️ Play simple games (like Google Pac-Man, Chrome Dino, Flappy Bird clones) hands-free!
- 🔁 Gesture cooldown control to prevent repeated actions
- 🔧 Easy to extend with more gestures (e.g., thumbs up, fist)

---

## 🛠️ Tech Stack

- Python
- [MediaPipe](https://google.github.io/mediapipe/)
- OpenCV
- PyAutoGUI

---

## 🖥️ How It Works

1. Captures video input from webcam using OpenCV
2. Uses MediaPipe to detect hand landmarks
3. Tracks movement of the index finger tip
4. Calculates swipe direction (based on delta `x` and `y`)
5. Sends keyboard key presses (`up`, `down`, `left`, `right`) using PyAutoGUI

---

## 📦 Installation

Make sure you have Python 3.7 or above.

# Clone the repository
git clone https://github.com/your-username/HandSwipe-Game-Controller.git
cd HandSwipe-Game-Controller

# Install dependencies
pip install opencv-python mediapipe pyautogui
▶️ Usage

python hand_swipe_controller.py
Move your index finger in a swipe direction.

Make sure your hand is visible and well-lit.

Press ESC to exit the app.

🎮 Try It On
🕹️ Google Pac-Man

🦖 Chrome Dino Game

🪁 Flappy Bird Clone

⚙️ Configuration
You can tweak:

swipe_threshold: Minimum distance in pixels to detect a swipe.

cooldown: Time in seconds to avoid repeated swipes.

swipe_threshold = 40   # Minimum movement to register a swipe
cooldown = 0.5         # Cooldown between gestures (in seconds)
📌 To-Do / Improvements
✋ Add gesture for 'pause' or 'click' using fist/thumb

🖼️ Add UI overlay to show gesture info

🎮 Full hand tracking game (mouse control, tap to shoot, etc.)

🌓 Add dark mode and overlay visuals

🧠 Inspiration
Inspired by the need for accessible, contactless game control — perfect for touch-free gameplay or experimenting with computer vision interfaces.

🙌 Contributing
Contributions, ideas, and feedback are welcome! Fork the repo and submit a pull request.

👨‍💻 Author
Devojeet Diwakar
GitHub 
