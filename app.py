from flask import Flask, render_template, request
import numpy as np
import pickle

# ===============================
# Load Trained Model
# ===============================
with open("heart_model.pkl", "rb") as file:
    model = pickle.load(file)

# ===============================
# Flask App
# ===============================
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from form
        input_features = [
            float(request.form["age"]),
            float(request.form["sex"]),
            float(request.form["cp"]),
            float(request.form["trestbps"]),
            float(request.form["chol"]),
            float(request.form["fbs"]),
            float(request.form["restecg"]),
            float(request.form["thalach"]),
            float(request.form["exang"]),
            float(request.form["oldpeak"]),
            float(request.form["slope"]),
            float(request.form["ca"]),
            float(request.form["thal"])
        ]

        # Convert to NumPy Array
        final_input = np.array([input_features])

        # Predict
        prediction = model.predict(final_input)[0]

        # Result
        if prediction == 1:
            result = "⚠ Heart Disease Detected"
        else:
            result = "✅ No Heart Disease Detected"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text="Error: " + str(e)
        )


# Run App
if __name__ == "__main__":
    app.run(debug=True)