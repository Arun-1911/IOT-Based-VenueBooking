from flask import Flask, render_template, request, redirect, url_for, flash, session
import datetime
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy credentials
users = {"faculty": "password123"}

# Booking storage
bookings = []

# Store live count (initialize to zero or a suitable default)
live_count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('booking'))
        else:
            flash('Wrong username or password.')
    return render_template('login.html')

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        email = request.form['email']
        flash('Reset link sent to your email.')
        return redirect(url_for('reset_sent'))
    return render_template('forgot.html')

@app.route('/reset_sent')
def reset_sent():
    return render_template('reset_sent.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        venue = request.form['venue']
        date_from = request.form['date_from']
        date_to = request.form['date_to']
        time_from = request.form['time_from']
        time_to = request.form['time_to']
        user = session['username']
        # Check for duplicate
        for b in bookings:
            if (b['venue'] == venue and b['date_from'] == date_from and b['time_from'] == time_from):
                flash('Venue already booked at this date/time.')
                return redirect(url_for('booking'))
        bookings.append({
            "user": user,
            "venue": venue,
            "date_from": date_from,
            "date_to": date_to,
            "time_from": time_from,
            "time_to": time_to
        })
        flash('Booking successful.')
        return redirect(url_for('booking'))
    return render_template('booking.html', bookings=bookings)

@app.route('/view_bookings')
def view_bookings():
    if 'username' not in session:
        return redirect(url_for('login'))
    user_bookings = [b for b in bookings if b['user'] == session['username']]
    return render_template('view_bookings.html', user_bookings=user_bookings)

@app.route('/live_count')
def live_count():
    try:
        response = requests.get("http://172.20.10.2/")  # IP of your ESP8266
        if response.status_code == 200:
            html = response.text
            count = html.split("People Count: ")[1].split("</h1>")[0]
            return render_template('live_count.html', count=count)
    except:
        return render_template('live_count.html', count="Unavailable")

# Route to update live count from ESP8266
@app.route('/update_live_count', methods=['POST'])
def update_live_count():
    global live_count
    venue = request.form['venue']
    count = request.form['count']
    try:
        live_count = int(count)
        return "Live count updated successfully", 200
    except ValueError:
        return "Invalid count", 400

if __name__ == "__main__":
    app.run(debug=True)
