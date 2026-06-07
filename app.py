import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🛠 Smart Analytics Tool")

# -------------------------
# 1. File Upload
# -------------------------
st.header("📂 Upload CSV File")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # -------------------------
    # 2. Dataset Preview
    # -------------------------
    st.header("📊 Dataset Preview")
    st.write(df.head())

    # -------------------------
    # 3. Missing Values
    # -------------------------
    st.header("❗ Missing Value Analysis")
    st.write(df.isnull().sum())

    # -------------------------
    # 4. Statistical Summary
    # -------------------------
    st.header("📈 Statistical Summary")
    st.write(df.describe())

    # -------------------------
    # 5. Dynamic Visualizations
    # -------------------------
    st.header("📊 Data Visualization")

    column = st.selectbox("Select Column for Visualization", df.columns)

    # Histogram
    fig1 = px.histogram(df, x=column, title=f"{column} Distribution")
    st.plotly_chart(fig1)

    # Box plot
    fig2 = px.box(df, y=column, title=f"{column} Box Plot")
    st.plotly_chart(fig2)

    # Scatter (if possible)
    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) >= 2:
        col1 = st.selectbox("X-axis", numeric_cols)
        col2 = st.selectbox("Y-axis", numeric_cols)

        fig3 = px.scatter(df, x=col1, y=col2, title=f"{col1} vs {col2}")
        st.plotly_chart(fig3)

else:
    st.warning("Please upload a CSV file to continue.")