import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Gun Violence for Counties in New Mexico")

# Use the file path for the dataset
file_path = 'Gun Violence for Counties.csv'

# Check if the file exists
try:
    # Read the CSV file
    data = pd.read_csv(file_path)
    st.write("### Data Preview")
    st.dataframe(data)

    # Lock the X-axis to "County"
    x_column = "County"
    if x_column not in data.columns:
        st.error(f"The dataset must contain a '{x_column}' column.")
    else:
        # Dropdown for selecting the Y-axis column
        y_column = st.selectbox(
            "Select Y-axis column",
            [
                "Deaths per 100,000 Population",
                "Gun Casualties",
                "Population Count Estimate"
            ]
        )

        # Plot button
        if st.button("Plot Bar Graph"):
            fig, ax = plt.subplots(figsize=(12, 8))

            # Bar chart with counties on the X-axis
            ax.bar(data[x_column], data[y_column])
            ax.set_title(f"{y_column} by County")
            ax.set_xlabel("County")
            ax.set_ylabel(y_column)
            plt.xticks(rotation=90, ha="right")  # Rotate x-axis labels for readability

            st.pyplot(fig)

    st.write("Tip: The X-axis is locked to 'County'. Use the dropdown to select the Y-axis column for meaningful insights.")

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please ensure the file is available in the specified location.")
