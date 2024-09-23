# Project Title: Gym Equipment Usage Monitoring System

## Goal Statement
To develop a system that utilizes video feeds to monitor gym equipment usage by identifying whether individuals are standing or sitting in designated areas. The system will update a database to reflect equipment availability, allowing users to check machine status via a front-end website.

---

## Diagram D0: High-Level Overview

### Description
This diagram provides a basic overview of the system, identifying the main input, processing, and output components.

#### Diagram Components
- **Boxes/Figures:**
  - **Camera**: Represents the video feed input.
  - **Processing Unit**: Indicates where video data is analyzed.
  - **Database**: Stores the equipment usage status.
  - **Front-End Website**: Displays the equipment availability to users.

- **Lines:**
  - Solid lines represent the flow of data between components.

---

## Diagram D1: Module/Subsystem Design

### Description
This diagram elaborates on the key modules identified in D0, detailing the functionality of each subsystem.

### Key Points
- **Camera Module**: Captures video feed and streams it to the Object Detection Module.
- **Object Detection Module**: Analyzes video frames for the presence and position of individuals.
- **State Tracking Module**: Determines if gym equipment is in use based on detection results, updating the Database Module.
- **Database Module**: Stores equipment status (in use/free) and timestamps. It also communicates with the User Interface Module.
- **User Interface Module**: Requests and displays the current status of gym equipment to the Front-End Website, allowing users to check equipment availability.

---