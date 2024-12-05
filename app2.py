import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Gun Violence for Counties in New Mexico")

# Use the file path from Colab
file_path = 'Gun Violence for Counties.csv'

# Check if the file exists
try:
    # Read the CSV file
    data = pd.read_csv(file_path)
    st.write("### Data Preview")
    st.dataframe(data)

    # Lock the X-axis to "County, New Mexico, United States" column
    x_column = "County, New Mexico, United States"
    if x_column not in data.columns:
        st.error("The dataset must contain a 'County, New Mexico, United States' column.")
    else:
        # Dropdown for selecting the Y-axis column
        y_column = st.selectbox(
            "Select Y-axis column",
            [
                "Deaths per 100,000 Population, Age-adjusted",
                "Gun Casualties",
                "Population Count Estimate"
            ]
        )

        # Plot button
        if st.button("Plot Bar Graph"):
            fig, ax = plt.subplots(figsize=(10, 6))

            # Bar chart with counties on the X-axis
            ax.bar(data[x_column], data[y_column])
            ax.set_title(f"{y_column} by County")
            ax.set_xlabel("County")
            ax.set_ylabel(y_column)
            plt.xticks(rotation=90, ha="right")  # Rotate x-axis labels for readability

            st.pyplot(fig)

    st.write("Tip: The X-axis is locked to counties. Use the dropdown to select the Y-axis column for meaningful insights.")

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please ensure the file is available in the Colab environment.")
