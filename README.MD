AI-Powered Student Management System

An intelligent web-based student management system that streamlines student data entry, performance tracking, score prediction using ML, and data analytics. Built with Flask, Pandas, Matplotlib, and integrated with Flask-Login for secure access.

🚀 Features

Feature

Description

🧑‍🎓 Add Student

Add student data with attendance, prior scores, and study hours

✏️ Edit/Delete Student

Modify or remove student records from the system

🤖 Predict Score

Use a machine learning model to estimate final exam score

📈 View Analytics

Top 5 performers and class average score/attendance

🔐 Login/Logout

Secure access with user authentication (Flask-Login)

🖥️ Dashboard

Clean Bootstrap UI with navigation and student list table

📁 Tech Stack

Backend: Flask, Pandas

Frontend: HTML, Bootstrap 5, Jinja2

ML Model: Trained on sample dataset (RandomForest / LinearRegression)

Authentication: Flask-Login (admin credentials only)

Analytics: Matplotlib (charts for score/attendance trends)

🛠️ How to Run Locally

Clone the Repository

git clone https://github.com/ronak171990/AI-Powered-Student-Management-System.git
cd AI-Powered-Student-Management-System

Set up Environment

python -m venv venv
venv\Scripts\activate         # On Windows
pip install -r requirements.txt

Run the Application

python app.py

Open in Browser

http://127.0.0.1:5000

🔑 Admin Login

Username

Password

admin

admin123

📊 Dataset Schema

CSV file: data/students.csv

id,name,attendance,previous_score,study_hours,final_score

🧠 Machine Learning

Inputs: attendance, previous_score, study_hours

Output: final_score

Pretrained model used from ml_model/predictor.py

📌 Folder Structure

project/
├── app.py
├── ml_model/
│   └── predictor.py
├── data/
│   └── students.csv
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   ├── predict.html
│   ├── charts.html
│   └── login.html
├── static/
│   └── (Bootstrap assets / charts)

🚧 Future Enhancements

Feature

Status

📄 Export student report

🔜 Planned

🧑‍💼 Multi-user roles

🔜 Planned

📦 SQLite/PostgreSQL DB

🔜 Planned

📱 Mobile-friendly design

🔜 Planned

📃 License

This project is licensed under the MIT License.

🙌 Acknowledgements

Built by Ronak Ambu Patel as part of the Artificial Intelligence/Machine Learning Internship at StaxTech.

"Empowering institutions with smarter student data and AI!"