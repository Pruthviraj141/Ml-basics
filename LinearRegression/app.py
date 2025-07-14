# linear_regression_app.py

import streamlit as st
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample Data
x = [[151], [174], [138], [186], [128], [136], [179], [163], [152], [131]]
y = [63, 81, 56, 91, 47, 57, 76, 72, 62, 48]

# Train the model
regressor = LinearRegression()
regressor.fit(x, y)

# Streamlit App
st.title("Height to Weight Prediction App")

# User Input
height = st.number_input("Enter height (cm):", min_value=100, max_value=200, value=150)

# Predict and plot
if st.button("Predict Weight"):
    predicted_weight = regressor.predict([[height]])[0]
    st.success(f"Predicted Weight: {predicted_weight:.2f} kg")

    # Plotting section
    fig, ax = plt.subplots()
    
    # Original data points
    ax.scatter([i[0] for i in x], y, color='blue', label='Original Data')
    
    # Regression line
    predicted_line = regressor.predict(x)
    ax.plot([i[0] for i in x], predicted_line, color='red', label='Regression Line')

    # User's prediction point
    ax.scatter(height, predicted_weight, color='green', s=100, label='Your Prediction')

    ax.set_xlabel("Height (cm)")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Height vs Weight Regression")
    ax.legend()
    ax.grid(True)

    # Display the plot in Streamlit
    st.pyplot(fig)
