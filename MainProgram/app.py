from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to connect to MySQL Database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chillicothe1",  # Update with your actual MySQL password
        database="gym_monitoring"
    )

# API Route to fetch equipment statuses
@app.route('/api/equipment_status', methods=['GET'])
def get_equipment_status():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT equipment_name, status FROM equipment_status"
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
