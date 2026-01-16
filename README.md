Overview

RoadWatch is an innovative road condition monitoring system designed to enhance the safety and efficiency of road infrastructure maintenance. It leverages cutting-edge technologies, including Artificial Intelligence (AI) and Computer Vision, to detect and classify road surface defects in real time, such as cracks, potholes, and other anomalies.

Features

1. Real-time defect detection using the YOLOv8 object detection system.
2. Capable of identifying cracks, potholes, and other road anomalies.
3. Incorporates Python libraries such as OpenCV, Winsound, and Tkinter for real-time recognition and user interface implementation.
4. Trained on a comprehensive dataset of 5,718 images containing 9,410 defect instances.

Installation

1. Clone the repository:
git clone <repository_url>
2. Install the required Python libraries:
pip install opencv-python winsound tk ultralytics
3. Download the trained YOLOv8 model (if not included in the repo).

Usage
1. Run the Python program:

python roadwatch.py

2. The system will detect and highlight road anomalies in real-time through the interface.
