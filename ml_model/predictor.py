import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

DATA_PATH = "data/students.csv"
MODEL_PATH = "ml_model/model.pkl"

def train_model():
    df = pd.read_csv(DATA_PATH)
    X = df[["attendance", "previous_score", "study_hours"]]
    y = df["final_score"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)
    print("✅ Model trained and saved to:", MODEL_PATH)

def predict_score(attendance, previous_score, study_hours):
    if not os.path.exists(MODEL_PATH):
        train_model()

    model = joblib.load(MODEL_PATH)
    input_data = [[attendance, previous_score, study_hours]]
    predicted = model.predict(input_data)[0]
    return round(predicted, 2)
