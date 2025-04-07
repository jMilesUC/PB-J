from flask import Flask, jsonify
import cv2
import torch
from yolov5 import YOLOv5

app = Flask(__name__)

# Load YOLOv5 Model
model = YOLOv5("runs/train/expX/weights/best.pt", device="cpu")

# Path to video file (or use 0 for webcam)
video_path = "path/to/gym_video.mp4"
cap = cv2.VideoCapture(video_path)

def get_equipment_status():
    ret, frame = cap.read()
    if not ret:
        return {"status": "No video feed"}

    # Run inference
    results = model(frame)
    detected_classes = [model.names[int(x)] for x in results.pred[0][:, -1]]

    # Equipment names based on your trained model
    equipment_status = {
        "Dumbbell Bench": "Open",
        "Treadmill": "Open",
        "Chest Bench": "Open"
    }

    # If a "person" is detected, mark the equipment as "In Use"
    if "person" in detected_classes:
        for equip in equipment_status.keys():
            if equip in detected_classes:
                equipment_status[equip] = "In Use"

    return equipment_status

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(get_equipment_status())

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
