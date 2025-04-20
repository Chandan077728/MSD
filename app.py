from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load trained model and preprocessing objects
model = joblib.load("models/rf_model.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")  # Fixed this line

# List of features used in training
features = [
    "programming", "maths", "communication", "logic",
    "self_learning", "projects_completed", "years_experience",
    "internships", "gpa"
]

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs and scale
        input_data = [float(request.form[feature]) for feature in features]
        input_scaled = scaler.transform([input_data])

        # Predict and get confidence
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]
        confidence = round(np.max(prediction_proba) * 100, 2)

        # Get top 3 suggested roles with confidence
        top_indices = np.argsort(prediction_proba)[::-1][:3]
        top_suggestions = [
            f"{label_encoder.inverse_transform([idx])[0]} ({round(prediction_proba[idx]*100, 2)}%)"
            for idx in top_indices
        ]

        return render_template(
            'result.html',
            prediction=label_encoder.inverse_transform([prediction])[0],
            confidence=confidence,
            suggestions=top_suggestions
        )

    except Exception as e:
        return f"❌ Error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
