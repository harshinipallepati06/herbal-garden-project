print("Running")
from flask import Flask, render_template, request
import pandas as pd
print("App")
app = Flask(__name__)

# Load Excel files
plants = pd.read_excel("data/plants.xlsx")
doctors = pd.read_excel("data/doctors.xlsx")

# Clean data (important)
plants['disease'] = plants['disease'].str.strip().str.lower()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    disease = request.form['disease'].lower()
    severity = request.form['severity']
    breathing = request.form['breathing']
    location = request.form['location'].lower()

    filtered_plants = plants[plants['disease'] == disease]

    # 👇 ADD HERE (doctor filtering)
    # Doctor filtering (improved)
    filtered_doctors = doctors[
        doctors['location'].str.strip().str.lower() == location.strip().lower()
        ]

# Convert to list
    doctors_list = filtered_doctors.head(6).to_dict(orient='records')

    return render_template(
        "result.html",
        disease=disease,
        severity=severity,
        breathing=breathing,
        location=location,
        plants=filtered_plants.to_dict(orient='records'),
        doctors=doctors_list
    )
if __name__ == '__main__':
    app.run(debug=True)