import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Gun Violence for Race and Gender")

# Load the data (replace this with your file path)
file_path = 'Gun Violence For Race and Gender.csv'

# Check if the file exists
try:
    # Read the CSV file
    data = pd.read_csv(file_path)
    st.write("### Original Data Preview")
    st.dataframe(data)

    # Preprocess data: Remove commas from numeric columns and convert to integers
    data['Count'] = data['Count'].str.replace(",", "").astype(int)
    data['Population Count Estimate'] = data['Population Count Estimate'].str.replace(",", "").astype(int)

    # Aggregate data by sex (e.g., sum the counts and population estimates)
    aggregated_data = data.groupby('Sex, M/F').agg({
        'Count': 'sum',
        'Population Count Estimate': 'sum'
    }).reset_index()

    # Display aggregated data
    st.write("### Aggregated Data by Gender")
    st.dataframe(aggregated_data)

    # Dropdown for selecting columns
    columns = aggregated_data.columns.tolist()
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    # Dropdown for graph type
    graph_type = st.selectbox(
        "Select Graph Type",
        ["Bar", "Pie"]
    )

    # Plot button
    if st.button("Plot Graph"):
        fig, ax = plt.subplots()

        if graph_type == "Bar":
            ax.bar(aggregated_data[x_column], aggregated_data[y_column])
            ax.set_title(f"{y_column} vs {x_column} (Bar Chart)")

        elif graph_type == "Pie":
            plt.pie(
                aggregated_data[y_column],
                labels=aggregated_data[x_column],
                autopct='%1.1f%%',
                startangle=90,
            )
            plt.title(f"{y_column} (Pie Chart)")

        if graph_type != "Pie":
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            st.pyplot(fig)
        else:
            st.pyplot(plt)

    st.write("Tip: Ensure the selected columns are numeric for meaningful plots.")

except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please ensure the file is available.")
