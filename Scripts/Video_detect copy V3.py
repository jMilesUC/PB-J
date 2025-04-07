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

# Dictionary to store cooldown timestamps for equipment (in seconds)
cooldowns = {}

# Set up mode and timing
mode = "detection"  # Start in detection mode
mode_start_time = time.time()
interval = 30  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    

    current_time = time.time()
    # Check if the current mode period has elapsed
    if current_time - mode_start_time >= interval:
        # Toggle mode between "detection" and "idle"
        mode = "no_detection" if mode == "detection" else "detection"
        mode_start_time = current_time
        print("Switched mode to:", mode)

    # If in detection mode, run detection on the frame
    if mode == "detection":
        results = model.predict(frame)
        try:
            # Access class names from the underlying model
            detected_classes = [model.model.names[int(cls)] for cls in results.pred[0][:, -1].tolist()]
        except Exception as e:
            print("Error during detection:", e)
            detected_classes = []

        # Determine if a person is detected
        person_detected = "person" in detected_classes

         # Update equipment status based on detection with cooldown logic
        for equipment in gym_equipment:
            # If equipment is detected and a person is present, mark as "in_use"
            if equipment in detected_classes and person_detected:
                update_equipment_status(equipment, "in_use")
                cooldowns[equipment] = current_time  # reset the cooldown timer
            else:
                # If equipment is not currently detected as in use
                if equipment in cooldowns:
                    # If the cooldown period (2 minutes) has not passed, continue showing "in_use"
                    if current_time - cooldowns[equipment] < 120:
                        update_equipment_status(equipment, "in_use")
                    else:
                        update_equipment_status(equipment, "available")
                        del cooldowns[equipment]
                else:
                    update_equipment_status(equipment, "available")
        # Render results on the frame
        results.render()  # Draw bounding boxes and labels

        # Always display the current frame
        cv2.imshow("Detection Results", frame)
    else:
        # Always display the current frame
        cv2.imshow("Detection Results", frame)

    # Check for the 'q' key to quit
    if cv2.waitKey(17) & 0xFF == ord('q'):
        break


# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
