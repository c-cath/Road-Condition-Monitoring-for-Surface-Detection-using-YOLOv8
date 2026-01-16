import cv2
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from ultralytics import YOLO

# Load your trained YOLOv8 model (adjust the path if needed)
model = YOLO("C:/Users/Catherina Dela Cruz/Desktop/RoadWatch_V1/best.pt")  # Replace with your actual model path

# Initialize Tkinter root window
root = Tk()
root.title("Road Watch App")
root.geometry("1300x800")  # You can adjust the window size

# Set up the video capture (webcam)
cap = None

# Function to process the webcam frames and run inference
def process_frame():
    ret, frame = cap.read()  # Capture a frame from the webcam
    if not ret:
        print("Failed to grab frame.")
        return
    
    # Perform inference on the frame
    results = model(frame)  # Run inference on the captured frame
    annotated_frame = results[0].plot()  # Get the annotated frame with bounding boxes

    # Convert the frame to RGB (OpenCV uses BGR by default)
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    # Convert the frame to an ImageTk format
    img = Image.fromarray(annotated_frame)
    imgtk = ImageTk.PhotoImage(image=img)

    # Update the image in the Tkinter window
    lbl.imgtk = imgtk
    lbl.configure(image=imgtk)

    # Call the function again after 10 ms to update the frame
    lbl.after(10, process_frame)

# Function to handle image selection from local storage
def select_image():
    # Open file dialog to manually select an image
    image_path = askopenfilename(
        title="Select an image", 
        initialdir="C:/Users/Catherina Dela Cruz/Downloads/CLASSES",  # Set the initial folder
        filetypes=[("Image Files", "*.jpg;*.png")]  # Allow only .jpg and .png files
    )

    if image_path:  # Check if the user selected a file
        print(f"Running inference on {image_path}")
        
        # Load the selected image
        image = cv2.imread(image_path)
        
        # Perform inference on the selected image
        results = model(image)  # Run inference on the selected image
        
        # Annotate the frame with detection results
        annotated_image = results[0].plot()  # Get the annotated frame with bounding boxes

        # Convert the frame to RGB (OpenCV uses BGR by default)
        annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

        # Convert the frame to an ImageTk format
        img = Image.fromarray(annotated_image)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the image in the Tkinter window
        lbl.imgtk = imgtk
        lbl.configure(image=imgtk)
    else:
        print("No image selected.")

# Function to start webcam feed
def start_webcam():
    global cap
    cap = cv2.VideoCapture(0)  # 0 is usually the default webcam

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return
    
    # Set the desired window size for webcam feed (e.g., 1280x720)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)  # Set width to 1280
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Set height to 720

    # Hide other options (we'll show webcam feed now)
    select_btn.pack_forget()
    webcam_btn.pack_forget()

    # Start processing the webcam frames
    process_frame()

# Create buttons for selecting image or using webcam
select_btn = Button(root, text="Select Image", command=select_image)
select_btn.pack(pady=10)

webcam_btn = Button(root, text="Use Webcam", command=start_webcam)
webcam_btn.pack(pady=10)

# Create a label to display the webcam feed or selected image in the Tkinter window
lbl = Label(root)
lbl.pack()

# Run the Tkinter main loop
root.mainloop()

# Release the webcam when the app is closed
if cap:
    cap.release()
cv2.destroyAllWindows()
