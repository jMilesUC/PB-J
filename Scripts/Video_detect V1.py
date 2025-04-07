from yolov5 import YOLOv5
import cv2
import mysql.connector
import time

# Pip installs
#pip install yolov5
#pip install opencv-python-headless yolov5

# Connect to MySQL Database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chillicothe1",  # Replace with your MySQL password
        database="gym_monitoring"
    )

# Update Equipment Status in MySQL
def update_equipment_status(equipment_name, status):
    conn = connect_db()
    cursor = conn.cursor()

    query = "UPDATE equipment_status SET status = %s WHERE equipment_name = %s"
    values = (status, equipment_name)
    cursor.execute(query, values)
    
    conn.commit()
    print(f"Updated: {equipment_name} - {status}")

    cursor.close()
    conn.close()

# Load the trained YOLOv5 model
model = YOLOv5(r"C:\Users\Parker Manson\Desktop\Senior Desgin\Yolo\yolov5\runs\train\exp11\weights\best.pt", device="cuda:0")

# Path to the video file
video_path = r"Z:\Senior Design\Validation_Videos\Bumbbell_Bench.mp4"

# Open the video file
cap = cv2.VideoCapture(video_path)

#Test to see if video opens properly
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Gym equipment classes and cooldown timers
gym_equipment = ["dumbbell_bench", "Treadmill", "Chest Bench"]
cooldown_timers = {equipment: 0 for equipment in gym_equipment}

while True:
    # AI sleeps for 30 seconds
    print("AI sleeping...")
    time.sleep(5)  #change back to 30

    # AI wakes for 30 seconds
    print("AI awake...")
    start_time = time.time()

    while time.time() - start_time < 30:
        ret, frame = cap.read()
        if not ret:
            print("end video")
            break  # End of video

        # Perform inference on the frame
        results = model.predict(frame)

        # Extract detected classes
        detected_classes = [model.model.names[int(cls)] for cls in results.pred[0][:, -1].tolist()]

        
        # Check for a "person"
        person_detected = "person" in detected_classes

        # Update equipment status
        current_time = time.time()
        for equipment in gym_equipment:
            if equipment in detected_classes and person_detected:
                update_equipment_status(equipment, "in_use")
                cooldown_timers[equipment] = current_time  # Reset cooldown timer
            elif current_time - cooldown_timers[equipment] > 120:  # 2-minute cooldown
                update_equipment_status(equipment, "not_in_use")

        # Render results on the frame
        results.render()  # Draw bounding boxes and labels

        # Display the processed frame
        cv2.imshow("Detection Results", frame)

        # Press 'q' to exit early
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if not ret:
        break  # End of video

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
