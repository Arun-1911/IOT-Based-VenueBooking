# Venue Booking System with IoT Integration

A database-driven web app built using **Flask** and **MySQL**, integrated with an **ESP8266 + IR sensor system** to track real-time venue occupancy.

---

## 📌 Features
- User authentication (register/login).  
- Venue booking and cancellation system.  
- Admin panel for managing venues.  
- IoT integration: ESP8266 + IR sensor tracks entry/exit.  
- Real-time live count displayed on the web dashboard.  

---

## 🛠 Prerequisites
Before running the project, make sure you have:

1. **Python 3.8+** installed → [Download here](https://www.python.org/downloads/)  
2. **Flask** and related dependencies (installed via `requirements.txt`).  
3. **MySQL database** running locally or remotely.  
4. **ESP8266 board + IR sensors** configured with provided Arduino code.  

---

## 🚀 Instructions

Follow these steps to set up and run the project in VS Code:

1. Clone the repository and enter the folder:  
   ```bash
   git clone https://github.com/your-username/venue-booking-system.git && cd venue-booking-system
Open a VS Code terminal:
Terminal → New Terminal

Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows (PowerShell):

bash
Copy code
.\venv\Scripts\Activate
On Windows (CMD):

bash
Copy code
venv\Scripts\activate.bat
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the database:

Create a MySQL database (e.g., venue_booking).

Import the schema from db/schema.sql.

Update database credentials in config.py.

Run the Flask app:

bash
Copy code
python app.py
Upload the ESP8266 Arduino code (in iot/esp8266_counter.ino) to your board and connect the IR sensors.

Open the web app in your browser:
http://127.0.0.1:5000

📊 System Architecture
Frontend: Flask (HTML, CSS, JS).

Backend: Flask + MySQL.

IoT Layer: ESP8266 + IR sensors for live count.

✅ Results
Users can book and manage venues online.

Admin can track all bookings.

Real-time occupancy automatically updates from IoT sensors.

