import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Firearm Injury Death Data Visualization App")

# Use the file path for the dataset
file_path = 'Firearm Injury Death by Year, New Mexico and U.S.csv'

# Check if the file exists
try:
    # Read the CSV file
    data = pd.read_csv(file_path)
    st.write("### Data Preview")
    st.dataframe(data)

    # Lock the X-axis to "Year"
    x_column = "Year"
    if x_column not in data.columns:
        st.error(f"The dataset must contain a '{x_column}' column.")
    else:
        # Dropdown for selecting the Y-axis column
        y_column = st.selectbox(
            "Select Y-axis column",
            [
                "Deaths per 100,000 Population, Age-adjusted",
                "Gun Casualties Per Year",
                "Population Count Estimate"
            ]
        )

        # Plot button
        if st.button("Plot Graph"):
            fig, ax = plt.subplots(figsize=(10, 6))

            # Bar chart with "Year" on the X-axis
            ax.bar(data[x_column], data[y_column])
            ax.set_title(f"{y_column} by {x_column}")
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability

            st.pyplot(fig)

    st.write("Tip: The X-axis is locked to 'Year'. Use the dropdown to select the Y-axis column for insights.")

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please ensure the file is available in the specified location.")
