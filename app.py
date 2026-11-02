
import streamlit as st
import pandas as pd
import numpy as np

# Application title
st.title("Automated EDA & Insights Generator")

st.write(
    "Upload your CSV file to automatically "
    "analyse your dataset."
)

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV file
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    # Display dataset
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Dataset information
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Rows", df.shape[0])

    with col2:
        st.metric("Total Columns", df.shape[1])

    with col3:
        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    # Descriptive statistics
    st.subheader("Descriptive Statistics")

    st.dataframe(
        df.describe(include="all").transpose()
    )

    # Missing values
    st.subheader("Missing Value Report")

    missing = df.isnull().sum()

    missing_report = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    st.dataframe(missing_report)

    # Duplicate records
    st.subheader("Duplicate Records")

    st.write(
        "Total duplicates:",
        df.duplicated().sum()
    )

else:
    st.info("Please upload a CSV file to begin.")
