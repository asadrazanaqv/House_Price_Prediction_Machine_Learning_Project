# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st


# Loading Model
loaded_model = pickle.load(open('trained_model.pkl', 'rb'))


# Creating a function for Prediciton
def house_price_prediction(input_data):
    # Changing The Data into Numpy Array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape The Array as we are Predicting
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    prediction_value = prediction[0]

    # Million format
    value_in_million = prediction_value / 10   # because 1 million = 10 lakh
    million_text = f"Your House Value is ${value_in_million:.7f} Million Dollars."

    return(million_text)



def main():
    
    #
    
    # Giving a title
    st.title('House Price Prediction Web App')
    
    # Getting the Data as input from user
    
    CRIM = st.text_input('Crime Rate (per capita by town)')
    ZN = st.text_input('Proportion of residential land zoned for large lots')
    INDUS = st.text_input('Proportion of non-retail business acres per town')
    CHAS = st.text_input('Charles River Dummy Variable (1=Yes, 0=No)')
    NOX = st.text_input('Nitric Oxides Concentration (pollution level)')
    RM = st.text_input('Average Number of Rooms per Dwelling')
    AGE = st.text_input('Proportion of owner-occupied units built before 1940')
    DIS = st.text_input('Weighted Distance to Boston Employment Centers')
    RAD = st.text_input('Index of Accessibility to Radial Highways')
    TAX = st.text_input('Full-Value Property Tax Rate per $10,000')
    PTRATIO = st.text_input('Pupil-Teacher Ratio by Town')
    B = st.text_input('B Feature (racial composition)')
    LSTAT = st.text_input('Percentage of lower status population')

    
    
    # Code for Prediction
    price_prediction = ''
    
    # Creating a Button
    
        
    if st.button('Prediction My House Price:'):
        # Convert all inputs to float
        try:
            input_data = ([float(CRIM), float(ZN), float(INDUS), float(CHAS), float(NOX), float(RM), float(AGE), float(DIS), float(RAD), float(TAX), float(PTRATIO), float(B), float(LSTAT)])
            
            price_prediction = house_price_prediction(input_data)
        except ValueError:
            price_prediction = "Please enter valid numeric values for all fields."
        
    st.success(price_prediction)
    
    
if __name__ == '__main__':
    main()
  