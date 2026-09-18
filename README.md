# OpenCV Lane Detection in Python (In Progress)

Using dashcam/webcam feed, detect and capture left and right lanes and draw them back to original frame in real time.

## What it does
Reads a dashcam video, applies grayscale conversion, Gaussian blur, and Canny edge detection, then masks the result to a triangular region of interest to isolate the road area.

## Tech used
Python, OpenCV, NumPy

## How to run it
pip install -r requirements.txt
python3 main.py

Place a dashcam or webcam video named DashCam10Sec.mp4 in the project root. Not included in this repo due to file size.

## Status
Edge detection and ROI masking complete. Next step is applying Hough transform to detect lane lines and drawing them back onto the original frame.

## Notes
Used a manually defined triangular mask to isolate the road region before edge detection, reducing noise from irrelevant parts of the frame.
