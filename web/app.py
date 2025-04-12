from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3


app = Flask(__name__)
app.secret_key = "dhdfhfdjh"

def init_db():
    conn = sqlite3.connect('microscope.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS specimens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        specimen_size REAL,
        actual_size REAL
    )
    ''')
    conn.commit()
    conn.close()

def save_specimen(username, specimen_size, actual_size):
    conn =  sqlite3.connect('microscope.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO specimens (username, specimen_size, actual_size) VALUES (?, ?, ?)',
                   (username, specimen_size, actual_size))
    conn.commit()
    conn.close()
    
def calculate_actual_size(specimen_size, magnification):
    return specimen_size * magnification
def main():
    username = input("Enter your username: ")
    specimen_size = float(input("Enter the specimen size in mm: "))
    magnification = float(input("Enter the microscope magnification: "))
    
    actual_size = calculate_actual_size(specimen_size, magnification)
    print(f"Actual size: {actual_size} mm")

if __name__ == "__main__":
    main()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    username = request.form['username']
    specimen_size = float(request.form['specimen_size'])
    magnification = float(request.form['magnification'])
    actual_size = calculate_actual_size(specimen_size, magnification)
    save_specimen(username, specimen_size, actual_size)
    flash(f"Real life size: {actual_size:.2f} mm", "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
