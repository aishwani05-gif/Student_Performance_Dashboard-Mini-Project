import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #dbeafe;
}

h1 {
    color: #1e3a8a;
    text-align: center;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Student Performance Dashboard")

df = pd.read_csv("data/students.csv")

df["Average"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
) / 3

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", len(df))

with col2:
    st.metric("Class Average", round(df["Average"].mean(), 2))

with col3:
    st.metric("Highest Average", round(df["Average"].max(), 2))

st.subheader("📋 Student Records")
st.dataframe(df)

st.subheader("📈 Average Marks")
st.bar_chart(df.set_index("Name")["Average"])

st.subheader("🎯 Attendance Analysis")
st.bar_chart(df.set_index("Name")["Attendance"])

st.subheader("🔍 Individual Student Analysis")

selected_student = st.selectbox(
    "Select Student",
    df["Name"]
)

student = df[df["Name"] == selected_student]

subject_marks = pd.DataFrame(
    {
        "Marks": [
            student["Maths"].values[0],
            student["Science"].values[0],
            student["English"].values[0]
        ]
    },
    index=["Maths", "Science", "English"]
)

st.bar_chart(subject_marks)

top_student = df.loc[df["Average"].idxmax()]

st.success(
    f"🏆 Top Performer: {top_student['Name']} | Average Marks: {top_student['Average']:.2f}"
)

st.info(
    "Built using Python, Pandas and Streamlit."
)