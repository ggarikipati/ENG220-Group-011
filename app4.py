# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Gun Violence for Race and Gender")

# Use the file path from Colab
file_path = 'Gun Violence For Race and Gender.csv'

# Check if the file exists
try:
    # Read the CSV file
    data = pd.read_csv(file_path)
    st.write("### Data Preview")
    st.dataframe(data)

    # Dropdown to select Sex
    sex = st.selectbox("Select Sex", ["Male", "Female", "Both"])

    # Filter data by selected Sex
    filtered_data = data[data["Sex"] == sex]

    # Dropdown to select the metric
    metric = st.selectbox(
        "Select Metric to Plot",
        ["Deaths per 100,000 Population, Age-adjusted", "Count", "Population Count Estimate"]
    )

    # Plot button
    if st.button("Plot Graph"):
        fig, ax = plt.subplots()

        # Bar chart of the selected metric for each race
        ax.bar(
            filtered_data["Race/Ethnicity"],
            filtered_data[metric]
        )
        ax.set_title(f"{metric} by Race/Ethnicity ({sex})")
        ax.set_xlabel("Race/Ethnicity")
        ax.set_ylabel(metric)
        plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability

        st.pyplot(fig)

    st.write("Tip: Use the dropdowns to select gender and metric for meaningful insights.")

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please ensure the file is available in the Colab environment.")
