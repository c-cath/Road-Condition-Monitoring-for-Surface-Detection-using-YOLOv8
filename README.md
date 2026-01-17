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

3. Install the required Python libraries:

pip install opencv-python winsound tk ultralytics

4. Download the trained YOLOv8 model (if not included in the repo).

Usage
1. Run the Python program:

python roadwatch.py

2. The system will detect and highlight road anomalies in real-time through the interface.

<img width="4000" height="400" alt="Screenshot 2025-01-09 183026" src="https://github.com/user-attachments/assets/8d864d6d-1c2b-4a7f-85a3-87ad67390b1c" />


<img width="1102" height="732" alt="Screenshot 2025-01-09 203216" src="https://github.com/user-attachments/assets/f0744493-977c-49e6-b365-c985228c8237" />


<img width="1102" height="732" alt="Screenshot 2025-01-09 183229" src="https://github.com/user-attachments/assets/08796896-ab0e-4840-93f5-ea33c72ed2ff" />

<img width="1102" height="732" alt="Screenshot 2025-01-09 183342" src="https://github.com/user-attachments/assets/002d3de6-1332-4839-91f3-0e57c4564d2c" />



