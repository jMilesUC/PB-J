import mysql.connector
import sys

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chillicothe1",  # Replace with your MySQL password if needed
        database="gym_monitoring"
    )

def add_equipment(equipment_name, status="available"):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO equipment_status (equipment_name, status) VALUES (%s, %s)"
        values = (equipment_name, status)
        cursor.execute(query, values)
        conn.commit()
        print(f"Added equipment: {equipment_name} with status: {status}")
    except Exception as e:
        print("Error adding equipment:", e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # Accept equipment name and an optional status from the command line.
    if len(sys.argv) < 2:
        print("Usage: python add_equipment.py <equipment_name> [status]")
        sys.exit(1)
    
    equipment_name = sys.argv[1]
    status = sys.argv[2] if len(sys.argv) > 2 else "available"
    
    add_equipment(equipment_name, status)
