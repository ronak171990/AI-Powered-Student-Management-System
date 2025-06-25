# AI-Powered Student Management System

from flask import Flask, render_template, request, redirect
import pandas as pd
import os
from ml_model.predictor import predict_score
import matplotlib.pyplot as plt
import io
import base64
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask import g

app = Flask(__name__)
DATA_PATH = "data/students.csv"

def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    else:
        return pd.DataFrame(columns=["id", "name", "attendance", "previous_score", "study_hours", "final_score"])

def save_data(df):
    df.to_csv(DATA_PATH, index=False)


@app.route('/')
def index():
    students = load_data().to_dict(orient='records')
    return render_template("index.html", students=students)

@app.route('/predict', methods=["GET", "POST"])
def predict():
    predicted = None
    if request.method == "POST":
        attendance = int(request.form["attendance"])
        previous_score = int(request.form["previous_score"])
        study_hours = float(request.form["study_hours"])

        #  Predict only – do not save or ask for name
        predicted = predict_score(attendance, previous_score, study_hours)

    return render_template("predict.html", predicted=predicted)

import matplotlib.pyplot as plt
import io
import base64

@app.route('/charts')
def charts():
    df = load_data()
    top_students = df.sort_values(by='final_score', ascending=False).head(5)

    names = top_students["name"].tolist()
    scores = top_students["final_score"].tolist()

    avg_score = df["final_score"].mean()
    avg_attendance = df["attendance"].mean()

    return render_template("charts.html", names=names, scores=scores,
                           avg_score=round(avg_score, 2), avg_attendance=round(avg_attendance, 2))


@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    df = load_data()
    df = df[df["id"] != student_id]
    save_data(df)
    return redirect("/")

@app.route('/edit/<int:student_id>', methods=["GET", "POST"])
def edit_student(student_id):
    df = load_data()
    student = df[df["id"] == student_id].to_dict(orient='records')
    if not student:
        return "Student not found", 404
    student = student[0]

    if request.method == "POST":
        df.loc[df["id"] == student_id, "name"] = request.form["name"]
        df.loc[df["id"] == student_id, "attendance"] = int(request.form["attendance"])
        df.loc[df["id"] == student_id, "previous_score"] = int(request.form["previous_score"])
        df.loc[df["id"] == student_id, "study_hours"] = float(request.form["study_hours"])
        
        # Update final score prediction
        predicted_score = predict_score(
            int(request.form["attendance"]),
            int(request.form["previous_score"]),
            float(request.form["study_hours"])
        )
        df.loc[df["id"] == student_id, "final_score"] = predicted_score

        save_data(df)
        return redirect("/")

    return render_template("edit.html", student=student)


app.secret_key = "ronak-secret-key"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Only one user for demo
users = {"admin": {"password": "admin123"}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            login_user(User(username))
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid credentials")
    
    return render_template("login.html")

@app.route('/add', methods=["GET", "POST"])
@login_required
def add_student():
    if request.method == "POST":
        df = load_data()
        new_id = df["id"].max() + 1 if not df.empty else 1

        attendance = int(request.form["attendance"])
        previous_score = int(request.form["previous_score"])
        study_hours = float(request.form["study_hours"])
        predicted_score = predict_score(attendance, previous_score, study_hours)

        new_student = {
            "id": new_id,
            "name": request.form["name"],
            "attendance": attendance,
            "previous_score": previous_score,
            "study_hours": study_hours,
            "final_score": predicted_score
        }

        df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
        save_data(df)
        return redirect("/")

    return render_template("add.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.context_processor
def inject_user():
    return dict(current_user=current_user)

if __name__ == "__main__":
    app.run(debug=True)