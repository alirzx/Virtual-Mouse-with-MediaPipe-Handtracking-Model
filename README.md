# Virtual Mouse with MediaPipe Hand Tracking

This project implements a **virtual mouse** using hand tracking powered by **MediaPipe**. It allows you to control your computer's mouse cursor using hand gestures captured via a webcam. The system detects your hand landmarks, tracks the index finger and thumb, and simulates mouse movements and clicks.

---
![Virtual Mouse Demo](images/virtual_mouse.png)

## Features

- **Hand Tracking**: Uses MediaPipe's Hand Tracking model to detect and track hand landmarks in real-time.
- **Mouse Control**: Moves the mouse cursor based on the position of your index finger.
- **Click Simulation**: Detects a pinch gesture (index finger and thumb close together) to simulate a mouse click.
- **Video Saving**: Saves the webcam feed with hand landmarks as a video file (`output.avi`).

---

## Requirements

To run this project, you need the following dependencies:

- Python 3.7 or higher
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- PyAutoGUI (`pyautogui`)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/alirzx/Virtual-Mouse-with-MediaPipe-Handtracking-Model.git
   cd Virtual-Mouse-with-MediaPipe-Handtracking-Model


## Code Overview
Key Components
MediaPipe Hands: Used for hand tracking and landmark detection.

OpenCV: Captures and processes the webcam feed.

PyAutoGUI: Controls the mouse cursor and simulates clicks.

Main Workflow
Initialize the webcam and MediaPipe Hand Tracking.

Capture frames from the webcam and detect hand landmarks.

Map the index finger's position to the screen and move the mouse cursor.

Detect a pinch gesture (index finger and thumb close together) to simulate a mouse click.

Save the webcam feed with hand landmarks as a video file.

# Example :
# Initialize MediaPipe Hands
```bash
capture_hands = mp.solutions.hands.Hands()

# Main loop
while True:
    _, image = cap.read()
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    res = capture_hands.process(rgb_image)
    hands = res.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_option.draw_landmarks(image, hand)
            # Process hand landmarks and control the mouse
