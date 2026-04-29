
# heart**
# Heart Disease Prediction System ❤️

A Machine Learning web application that predicts the likelihood of heart disease using patient medical data. This project is built with **Python**, **Flask**, **Scikit-learn**, and deployed using Render.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help in prevention and timely treatment.

This project uses a trained Machine Learning model to analyze medical parameters and predict whether a patient is at risk of heart disease.

---

## 🚀 Features

* Predict heart disease risk instantly
* User-friendly web interface
* Trained ML classification model
* Fast Flask backend
* Ready for deployment on Render
* Beginner-friendly project structure

---

## 📊 Dataset Features

The model uses the following input attributes:

* Age
* Sex
* Chest Pain Type (cp)
* Resting Blood Pressure (trestbps)
* Cholesterol (chol)
* Fasting Blood Sugar (fbs)
* Rest ECG (restecg)
* Maximum Heart Rate (thalach)
* Exercise Induced Angina (exang)
* Oldpeak
* Slope
* Number of Major Vessels (ca)
* Thalassemia (thal)

Target:

* 0 = No Heart Disease
* 1 = Heart Disease

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML
* CSS
* Gunicorn

---

## 📁 Project Structure

```bash
heart-disease-project/
│── app.py
│── train_model.py
│── requirements.txt
│── Procfile
│── runtime.txt
│── README.md
│── heart_model.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/heart-disease-project.git
cd heart-disease-project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## 🤖 Model Training

Train the model using:

```bash
python train_model.py
```

This creates:

```bash
heart_model.pkl
```

---

## 🌐 Deployment

Deploy easily on Render:

* Connect GitHub repository
* Build Command:

```bash
pip install -r requirements.txt
```

* Start Command:

```bash
gunicorn app:app
```

---

## 📈 Future Improvements

* Improve model accuracy
* Add XGBoost / Random Forest tuning
* Add patient report download
* Add dashboard analytics
* Add login system
* Add doctor recommendation module

---

## 👨‍💻 Author

Developed by Prasa.

---

## 📜 License

This project is for educational and learning purposes.
