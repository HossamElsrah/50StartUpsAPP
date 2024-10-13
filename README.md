# 50StartUpsAPP
Startup Profit Prediction

This project focuses on predicting the profit of startups using data from 50 startups, with features such as R&D Spend, Marketing Spend, Administration, and State. The model is built using a tree-based approach and achieves an accuracy of 99%.

Features

Dataset: Includes 50 records with columns:

State: The location of the startup.

R&D Spend: Investment in research and development.

Marketing Spend: Advertising and marketing expenses.

Administration: Administrative expenses.

Profit: Target variable for prediction.


Data Preprocessing: Includes data cleaning, EDA (Exploratory Data Analysis), renaming columns, detecting and handling outliers, and feature selection.

Model: Uses a tree-based algorithm to predict startup profits, achieving a 99% accuracy rate.

Deployment: The model and its pipeline are saved for integration into a Streamlit app, which allows users to input values for R&D Spend, Marketing Spend, Administration, and State to predict the expected profit.


How to Use

1. Clone the repository.


2. Install the required dependencies.


3. Run the Streamlit app using:

streamlit run app.py


4. Input the R&D Spend, Marketing Spend, Administration costs, and State.


5. Get the profit prediction for your startup!

