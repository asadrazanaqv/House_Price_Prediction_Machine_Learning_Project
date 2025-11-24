# 🏠 House Price Prediction Machine Learning Project

This project demonstrates how to build a **Machine Learning model** to predict house prices based on multiple factors such as area, number of rooms, and location.  
It covers the entire ML workflow — from **data cleaning** to **model evaluation**, **prediction visualization**, and **live web deployment using Streamlit**.

---

## 🌐 Live App
The project is now live! You can access the **interactive house price prediction app** here:  
[**Open in Streamlit Cloud**](https://housepricepredictionmachinelearningproject-3cxxq3lkx5qp96fabmc.streamlit.app/)

---

## 🚀 Project Overview
The main goal of this project is to use **Regression Algorithms** to accurately predict the price of houses.  
By training the model on existing data, it learns the relationship between different features (like area, rooms, etc.) and the target variable (price).  
The trained model is saved using **pickle** and deployed on **Streamlit Cloud**, making it accessible online for live predictions.

---

## 🧠 Machine Learning Workflow

1. **Data Collection & Loading**  
   - Imported dataset (CSV file) containing house attributes and prices.  
2. **Data Preprocessing**  
   - Handled missing values and outliers.  
   - Encoded categorical variables.  
   - Scaled numerical features for better model performance.  
3. **Exploratory Data Analysis (EDA)**  
   - Used **Matplotlib** and **Seaborn** to visualize relationships between features.  
   - Found key insights from correlation and distribution plots.  
4. **Model Training & Saving**  
   - Implemented **Linear Regression** using **Scikit-learn**.  
   - Split data into training and testing sets.  
   - Saved trained model using **pickle** for reuse in the Streamlit app.  
5. **Live Deployment using Streamlit**  
   - Created an interactive web app for house price prediction.  
   - Users can input house features and get **real-time predictions**.  
   - Deployed the app on **Streamlit Cloud**, making it accessible online.  
6. **Model Evaluation**  
   - Measured performance using **R² score**, **Mean Absolute Error (MAE)**, and **Root Mean Squared Error (RMSE)**.  

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|----------|
| **Python** | Core programming language |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical computation |
| **Scikit-learn** | Machine Learning modeling |
| **XGBoost** | Advanced regression modeling |
| **Matplotlib** / **Seaborn** | Data visualization |
| **Pickle** | Model serialization |
| **Streamlit** | Interactive web app deployment |
| **Spyder IDE** | Local development environment |

---

## 📈 Results
The trained model achieved a strong correlation between predicted and actual house prices, proving its usefulness in real-world scenarios like property valuation and real estate forecasting.  
The live app allows users to test predictions with their own inputs, making it practical and user-friendly.

---

## 🗂️ Project Structure

