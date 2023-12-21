import streamlit as st
import pandas as pd

# Streamlit app title
st.title("Upload and Calculate Mean")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)

    # Display the dataset
    st.write("Uploaded Dataset:")
    st.write(df)

    # Choose a column for mean calculation
    selected_column = st.selectbox("Select a column for mean calculation", df.columns)

    # Calculate and display the mean of the selected column
    mean_value = df[selected_column].mean()
    st.write(f"Mean of {selected_column}: {mean_value}")
