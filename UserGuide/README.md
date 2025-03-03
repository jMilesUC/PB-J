# 📘 Gym Equipment Monitoring System – User & Admin Guide

## 📑 Table of Contents
1. [End User Guide (For Gym Members)](#end-user-guide)
2. [Admin Guide (For Gym Owners & Managers)](#admin-guide)
   - [Installation Guide](#installation-guide)
   - [System Usage](#system-usage)
   - [FAQ](#faq)
   - [Troubleshooting](#troubleshooting)

---

# 🏋️ End User Guide (For Gym Members)

### **📌 Overview**
The **Gym Equipment Monitoring System** allows you to check which equipment is **available** or **in use** through an online webpage.

### **🖥️ How to Use the Webpage**
1. Open the gym’s **equipment status webpage** (URL will be provided by your gym).
2. You will see a list of gym equipment.
   - 🟢 **Green** = Available  
   - 🔴 **Red** = In Use  
3. Refresh the page to get the latest status.
4. If a machine is marked "in use" but is actually free, wait a few minutes— the system updates automatically.

### **❓ FAQ for Gym Members**
| Question | Answer |
|----------|--------|
| **How often does the status update?** | Every **30 seconds**. If no one is detected on the equipment for **2 minutes**, it will be marked "available." |
| **I see an error on the webpage. What should I do?** | Contact the gym staff; they can reset the system. |
| **How accurate is the system?** | It relies on a camera and AI detection. Sometimes, it may take a few seconds to update. |

---

# 🏢 Admin Guide (For Gym Owners & Managers)

## 🔧 Installation Guide

### **Prerequisites**
- **Python 3.8+**
- **MySQL Server**
- **YOLOv5 installed**
- **OpenCV installed** (`opencv-python-headless`)
- **A running web server** (to display the webpage)

### **Installation Steps**
1. Clone the project:
   ```sh
   git clone https://github.com/your-repo/gym-equipment-monitor.git
   cd gym-equipment-monitor
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up MySQL:
   - Create a database: **`gym_monitoring`**
   - Import `database_schema.sql` (provided in the repo)
   - Update `Video_detect.py` with your MySQL credentials.

4. Ensure the YOLOv5 model is in the correct location:
   ```sh
   C:\Users\Parker Manson\Desktop\Senior Design\Yolo\yolov5\runs\train\exp11\weights\best.pt
   ```
5. Run the detection system:
   ```sh
   python Video_detect.py
   ```
6. Deploy the **web dashboard**:
   - Host a simple Flask or PHP page that reads from the `equipment_status` table.
   - Gym members can visit the webpage to see real-time updates.

---

## 📊 System Usage

### **🎥 Running the Detection System**
- The system will process the **video feed** and detect gym equipment usage.
- Status is updated in the **`equipment_status`** table in MySQL.

### **📝 How the Detection Works**
1. If **a person is detected on a machine**, it is marked **"in_use"**.
2. If **no one is detected for 2 minutes**, it is marked **"available"**.
3. The system updates every **30 seconds**.

### **⚙️ Customization**
Want to add **new equipment types**?  
Edit the list in `Video_detect.py`:
```python
gym_equipment = ["dumbbell_bench", "Treadmill", "Chest Bench", "New Machine"]
```

Want to change the **cooldown time**?  
Edit this part in `Video_detect.py`:
```python
if current_time - cooldowns[equipment] < 120:
```
Change `120` to your preferred duration (in seconds).

---

## ❓ FAQ (For Admins)
| Issue | Solution |
|-------|----------|
| **Video file won’t open** | Check the `video_path` in `Video_detect.py`. |
| **MySQL connection error** | Ensure MySQL is running and credentials are correct. |
| **YOLO model not found** | Verify the model path in `Video_detect.py`. |
| **Equipment status not updating** | Check MySQL logs and error messages. |
| **Webpage not displaying data** | Ensure your web server is running and connected to the database. |

---

## 🚀 Future Improvements
- **Live video streaming** on the webpage.
- **Mobile app support** for easier access.
- **Automatic notifications** when equipment is available.

---

