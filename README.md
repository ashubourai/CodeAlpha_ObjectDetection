# 🚀 CodeAlpha_ObjectDetection

## Task 4: Detecting Objects In Real-Time from Video Streams via YOLOv8

This project is part of my AI Internship with [CodeAlpha](https://www.codealpha.tech). It implements real-time object detection using **YOLOv8** and **OpenCV** on video streams.

---

## ✨ Features

- Implementation of Object Detection using YOLOv8 (Nano Version)

- Processes video files (with no latency in comparison to webcam processing)

- Outputs the processed video with bounding boxes on detected objects

---

## 🖥️ Demo Video

🎥 will be update after the post on LinkedIn

---

## 🛠️ How to Run Locally

1. Clone this repo:

    ```bash

    git clone https://github.com/ashubourai/CodeAlpha_ObjectDetection.git

    cd CodeAlpha_ObjectDetection

    ```

2. Install required packages:

    ```bash

    pip install -r requirements.txt

    ```

3. Download YOLOv8n.pt Model:

    - [Download yolov8n.pt](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt)

    - Place it in the project directory.

4. Add a video file:

    - Place any `.mp4` video in the folder.

    - Rename it to `sample_video.mp4`.

5. Run the script:

    ```bash

    python object_detection_video.py

    ```

6. The output will be saved as `output.avi`.

---

## 📂 Folder Structure

