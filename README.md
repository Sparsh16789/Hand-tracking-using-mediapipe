# Hand Tracking and Landmark Detection using OpenCV and MediaPipe

This project implements a real-time hand tracking and landmark detection system using OpenCV for video capture and MediaPipe for processing and drawing hand landmarks. The system detects hand gestures in a video stream and displays real-time coordinates for each hand landmark along with the frame rate (FPS).

## Features

- **Real-time hand tracking** using your webcam.
- **Hand landmark detection** with detailed coordinate extraction.
- **Landmark drawing and hand connection visualization** on the video feed.
- **FPS calculation** to monitor real-time performance.
  
## Prerequisites

Before running the project, make sure the following Python libraries are installed:

- [OpenCV](https://pypi.org/project/opencv-python/): for video capturing and image processing.
- [MediaPipe](https://pypi.org/project/mediapipe/): for hand detection and drawing utilities.

To install these dependencies, run the following command in your terminal:

```bash
pip install opencv-python mediapipe
