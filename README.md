# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project builds an end-to-end machine learning system to predict house prices based on property features such as area, number of rooms, amenities, and furnishing status.

The project demonstrates the complete ML lifecycle:

* Data preprocessing
* Feature engineering
* Model training
* Evaluation
* Deployment using a Streamlit web application

---

## 🎯 Objectives

* Predict house prices using structured tabular data
* Apply feature engineering to improve model performance
* Compare machine learning models
* Build a deployable ML application

---

## 📊 Dataset

The dataset contains housing data with features such as:

* Area
* Bedrooms
* Bathrooms
* Stories
* Parking
* Main road access
* Air conditioning
* Furnishing status
* Preferred area

Target variable:

* **Price**

---

## ⚙️ Data Preprocessing

Steps performed:

* Converted categorical variables (yes/no) into numerical format
* Applied one-hot encoding to furnishing status
* Handled missing values
* Created new engineered features

---

## 🧠 Feature Engineering

To improve model performance, additional features were created:

* **Total Rooms** = Bedrooms + Bathrooms
* **Area per Room** = Area / Total Rooms
* **Luxury Score** = Combination of amenities like AC, guestroom, basement, etc.

These features help capture property quality and living conditions.

---

## 🤖 Machine Learning Models

### Linear Regression

* Used as a baseline model

### Random Forest Regressor

* Final selected model
* Handles non-linear relationships effectively
* Provides feature importance insights

---

## 📈 Model Performance

| Metric   | Value      |
| -------- | ---------- |
| MAE      | ~1,016,000 |
| R² Score | ~0.61      |

---

## 🔎 Model Insights

* **Area** is the most influential feature
* Amenities significantly impact house price
* Feature engineering improved prediction quality

---

## ⚠️ Limitations

* Dataset is relatively small (~545 samples)
* Lack of location-specific features reduces predictive power
* Model performance is constrained by available data

---

## 🚀 Streamlit Web Application

An interactive web application was built using Streamlit.

### Features:

* User inputs property details
* Real-time price prediction
* Simple and intuitive UI

Run locally:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
house-price-prediction/
│
├── app.py
├── house_model.pkl
├── house_price.ipynb
├── data/Housing.csv
└── README.md
```

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

---

## 💼 Key Learnings

* End-to-end ML pipeline development
* Feature engineering for tabular data
* Model evaluation and interpretation
* Deploying ML models as web applications

---

## 👨‍💻 Author

**Pawan Nikam**

Final-year engineering student
Interested in:

* Data Science
* Machine Learning
* AI Systems
* Embedded + FPGA-based AI

---
