
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the model and pipeline
tree = joblib.load('tree.apk')
full_pipline = joblib.load('full_pipline.apk')  # Corrected the file name to 'full_pipeline.apk'

# Load the data
startups = pd.read_csv('new_50startups.csv')

# Title
st.title('50 Startups Profit Prediction')
st.write('This App predicts the Startups Profit')

# Take input from user
RD_Spend = st.slider('R&D_Spend', float(startups['R&D_Spend'].min()), float(startups['R&D_Spend'].max()))
Administration = st.slider('Administration', float(startups['Administration'].min()), float(startups['Administration'].max()))
Marketing_Spend = st.slider('Marketing_Spend', float(startups['Marketing_Spend'].min()), float(startups['Marketing_Spend'].max()))
State = st.selectbox('State', ('New York', 'California', 'Florida'))

# Store the inputs as a dictionary
user_inputs = {
    'R&D_Spend': RD_Spend,
    'Administration': Administration,
    'Marketing_Spend': Marketing_Spend,
    'State': State
}

# Transform the data into a DataFrame
features = pd.DataFrame(user_inputs, index=[0])  

# Pipeline transformation
features_prepared = full_pipline.transform(features)

# Predictions
prediction = tree.predict(features_prepared)[0]

# Display the prediction
st.subheader('Prediction:')
st.markdown(f'### $ {round(prediction, 2)}')  
