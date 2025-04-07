import cv2
import torch
from yolov5 import YOLOv5

# Pip installs
#pip install yolov5
#pip install opencv-python-headless yolov5

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp5/weights/best.pt')

# Open a connection to the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam; change to video file path if needed

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    # Perform inference
    results = model(frame)

    # Render results on the frame
    frame_with_boxes = results.render()[0]

    # Display the frame with detections
    cv2.imshow('YOLOv5 Detection', frame_with_boxes)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
