import cv2
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from ultralytics import YOLO
import winsound 


model = YOLO("C:/Users/Catherina Dela Cruz/Desktop/RoadWatch_V1/best.pt") 

root = Tk()
root.title("Road Condition Monitoring for Surface Detection")
root.geometry("1100x700") 

cap = None

def process_frame():
    ret, frame = cap.read()  
    if not ret:
        print("Failed to grab frame.")
        return
    
    results = model(frame)  
    annotated_frame = results[0].plot()  

    confidence_threshold = 0.3

    anomalous_class_detected = False
    for detection in results[0].boxes.data:
        class_id = int(detection[5])  
        confidence = float(detection[4]) 
        
        if class_id == 0 and confidence >= confidence_threshold:  
            anomalous_class_detected = True
            break

    if anomalous_class_detected:
        winsound.Beep(1000, 500)  

    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(annotated_frame)
    imgtk = ImageTk.PhotoImage(image=img)

    lbl.imgtk = imgtk
    lbl.configure(image=imgtk)

    lbl.after(10, process_frame)


def select_image():
   
    image_path = askopenfilename(
        title="Select an image", 
        initialdir="C:/Users/Catherina Dela Cruz/Downloads/photos_anomalous_normal",  
        filetypes=[("Image Files", "*.jpg;*.png")] 
    )

    if image_path: 
        print(f"Running inference on {image_path}")
        
        image = cv2.imread(image_path)
        
        results = model(image)  
        
        annotated_image = results[0].plot()  

        anomalous_class_detected = False
        for detection in results[0].boxes.data:
            class_id = int(detection[5]) 
            confidence = float(detection[4])  
            print(f"Detected class ID: {class_id} with confidence: {confidence}") 

            if class_id == 0 and confidence >= 0.3: 
                anomalous_class_detected = True
                break
        
        if anomalous_class_detected:
            winsound.Beep(1000, 500)  

        annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

        img = Image.fromarray(annotated_image)
        imgtk = ImageTk.PhotoImage(image=img)

        lbl.imgtk = imgtk
        lbl.configure(image=imgtk)

        lbl.config(width=img.width, height=img.height)

    else:
        print("No image selected.")


def start_webcam():
    global cap
    cap = cv2.VideoCapture(0)  

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  

    select_btn.pack_forget()
    webcam_btn.pack_forget()

    process_frame()

window_width = 1200  
window_height = 900  

left_frame_width = int(window_width * 0.25)  
left_frame = Frame(root, bg="black", width=left_frame_width, height=window_height)  
left_frame.pack(side="left", fill="y", padx=0, pady=0)  

logo_image = Image.open("C:/Users/Catherina Dela Cruz/Downloads/RoadWatchLogo.png") 
logo_image = logo_image.resize((400, 400), Image.Resampling.LANCZOS)  
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = Label(left_frame, image=logo_photo, bg="black")
logo_label.pack(pady=20)  

button_frame = Frame(left_frame, bg="black")
button_frame.pack(pady=20) 

right_frame_width = window_width - left_frame_width 
right_frame = Frame(root, bg="goldenrod", width=right_frame_width, height=window_height)  
right_frame.pack(side=RIGHT, fill="y", padx=0, pady=0) 

lbl = Label(right_frame)
lbl.pack(padx=20, pady=20) 

right_frame_width = window_width - left_frame_width  
right_frame = Frame(root, bg="goldenrod", width=right_frame_width, height=window_height)  
right_frame.pack(side=RIGHT, fill="both", padx=0, pady=0)  
right_frame.pack_propagate(False)  


select_btn = Button(
    button_frame, 
    text="Select Image", 
    command=select_image, 
    bg="goldenrod", 
    fg="black", 
    font=("Arial", 12, "bold"),  
    width=25,  
    padx=5, 
    pady=5
)
select_btn.pack(pady=10)  


webcam_btn = Button(
    button_frame, 
    text="Open Webcam", 
    command=start_webcam, 
    bg="goldenrod", 
    fg="black", 
    font=("Arial", 12, "bold"),  
    width=25, 
    padx=5, 
    pady=5
)
webcam_btn.pack(pady=10)  

exit_btn = Button(
    button_frame,  
    text="Exit", 
    command=root.quit,  
    bg="goldenrod",  
    fg="black", 
    font=("Arial", 12, "bold"),  
    width=25, 
    padx=5, 
    pady=5
)
exit_btn.pack(pady=10)  

root.mainloop()

if cap:
    cap.release()
cv2.destroyAllWindows()
