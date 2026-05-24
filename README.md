🏠 House Rent Prediction using Machine Learning
📌 Project Overview

This project predicts house rental prices based on property features such as BHK, size, number of bathrooms, furnishing status, city, and area type. The objective is to build an accurate regression model that helps estimate monthly rent using machine learning techniques.

The project covers the complete machine learning workflow, including data cleaning, exploratory data analysis (EDA), feature engineering, model building, evaluation, and deployment-ready model saving.

🎯 Objectives
Analyze factors affecting house rental prices.
Perform data preprocessing and feature engineering.
Build and compare multiple regression models.
Implement Linear Regression from scratch.
Evaluate model performance using standard regression metrics.
Save trained models for future deployment.
📂 Dataset Features
Original Features
BHK
Size
Bathroom
Furnishing Status
City
Area Type
Rent
Engineered Features
Rent_per_sqft
Size_per_BHK
Bathroom_BHK_ratio
Is_Furnished
Is_Semi_Furnished
City_encoded
Area_Type_encoded
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
📊 Exploratory Data Analysis

The project includes:

Rent distribution analysis
Outlier detection and removal
City-wise rent comparison
Furnishing status analysis
BHK and size impact on rent
Correlation analysis
🤖 Machine Learning Models
Custom Implementation
Linear Regression from Scratch (Normal Equation)
Scikit-Learn Models
Linear Regression
Ridge Regression
Lasso Regression
Polynomial Regression
📈 Evaluation Metrics

Models are evaluated using:

R² Score
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
🚀 Model Training Workflow
Data Cleaning
Outlier Removal using IQR
Feature Engineering
Feature Scaling using StandardScaler
Train-Test Split
Model Training
Model Evaluation
Model Saving
