import streamlit as st
import pandas as pd
from main import run_pipeline

st.title("🌱 Green AI Model Comparison Dashboard")

uploaded_file = st.file_uploader(
    "📂 Upload your dataset (CSV)",
    type=["csv"]
)

TARGET_COLUMN = st.text_input("Enter Target Column Name")

if uploaded_file and TARGET_COLUMN:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    results_df = run_pipeline(df, TARGET_COLUMN)

    st.subheader("📊 Model Comparison Results")
    st.dataframe(results_df)

    st.success("✅ Analysis completed successfully")
