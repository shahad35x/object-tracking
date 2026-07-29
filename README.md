# Object Tracking 

A Python program that watches a live webcam feed and automatically draws a box around anything that moves, without needing to select a color or an object by hand similar to how a surveillance camera flags motion.


## How It Works

- **Background subtraction**: `cv2.createBackgroundSubtractorMOG2()` learns what the static background looks like from the live video, frame by frame.
- **Motion mask**: for every new frame, the background subtractor compares it to what it has learned and outputs a black-and-white mask white pixels mark where something changed (motion), black pixels mark the static background.
- **Cleaning the mask**: `cv2.threshold()` removes the gray "shadow" pixels the subtractor also detects, keeping only real motion.
- **Finding objects**: `cv2.findContours()` finds the outline of each white blob in the mask. Blobs smaller than `MIN_AREA` are ignored (camera noise), and a green box is drawn around the rest with `cv2.rectangle()`.

## Files

- `object_tracking.py` opens the webcam, detects motion, and draws a box around anything moving

## Setup & Running

**1. Create a Conda environment:**
```bash
conda create -n opencv-tracking python=3.11 -y
conda activate opencv-tracking
```

**2. Install OpenCV:**
```bash
pip install opencv-python
```

**3. Run it:**
```bash
python object_tracking.py
```
Two windows will open: the live camera feed with green boxes around moving objects and the black and white motion mask.
Move an object in front of your camera  or move yourself tracking will start automatically as soon as it detects motion.

Press `x` to quit.
