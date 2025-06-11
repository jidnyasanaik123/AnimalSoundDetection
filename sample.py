import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
def load_data():
    return pd.read_csv("children_sound_recognition_data.csv")

# Load the data
data = load_data()

# Convert 'Date' column to datetime
data["Date"] = pd.to_datetime(data["Date"], errors='coerce')

# Streamlit dashboard
st.title("Children's Animal Sound Recognition Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
children = st.sidebar.multiselect("Select Children", options=data["Child"].unique(), default=data["Child"].unique())
date_range = st.sidebar.date_input("Select Date Range", [data["Date"].min().date(), data["Date"].max().date()])

# Filter data based on user input
filtered_data = data.dropna(subset=["Date"])
filtered_data = filtered_data[(filtered_data["Child"].isin(children)) & (filtered_data["Date"].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))]

# Display filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_data)

# Metrics
st.subheader("Key Metrics")

total_tests = len(filtered_data)
avg_correct_identifications = filtered_data["Correctly Identified"].mean()
avg_pronunciation_accuracy = filtered_data["Pronunciation Accuracy (%)"].mean()

st.metric("Total Tests Conducted", total_tests)
st.metric("Average Correct Identifications", round(avg_correct_identifications, 2))
st.metric("Average Pronunciation Accuracy (%)", f"{round(avg_pronunciation_accuracy, 2)}%")

# Visualization
st.subheader("Visualizations")

# Bar chart for daily progress
st.subheader("Daily Progress")
daily_progress = filtered_data.groupby("Date")["Correctly Identified"].mean()
fig, ax = plt.subplots(figsize=(10, 6))
daily_progress.plot(kind="bar", ax=ax, title="Daily Average Correct Identifications", xlabel="Date", ylabel="Average Count")
st.pyplot(fig)

# Weekwise progress
st.subheader("Weekwise Progress")
filtered_data["Week"] = filtered_data["Date"].dt.to_period("W")
weekwise_progress = filtered_data.groupby("Week")["Correctly Identified"].mean()
fig, ax = plt.subplots(figsize=(10, 6))
weekwise_progress.plot(kind="bar", ax=ax, title="Weekwise Average Correct Identifications", xlabel="Week", ylabel="Average Count")
st.pyplot(fig)

# Monthwise progress
st.subheader("Monthwise Progress")
filtered_data["Month"] = filtered_data["Date"].dt.to_period("M")
monthwise_progress = filtered_data.groupby("Month")["Correctly Identified"].mean()
fig, ax = plt.subplots(figsize=(10, 6))
monthwise_progress.plot(kind="bar", ax=ax, title="Monthwise Average Correct Identifications", xlabel="Month", ylabel="Average Count")
st.pyplot(fig)

# Line graph for child-wise performance over time
st.subheader("Child-wise Performance Over Time")
child_performance_time = filtered_data.groupby(["Date", "Child"])["Correctly Identified"].mean().unstack()
fig, ax = plt.subplots(figsize=(10, 6))
child_performance_time.plot(kind="line", ax=ax, title="Child-wise Average Correct Identifications Over Time", xlabel="Date", ylabel="Average Correct Identifications")
st.pyplot(fig)

# Line graph for pronunciation accuracy over time
st.subheader("Pronunciation Accuracy Over Time")
pivot_data = filtered_data.pivot_table(index="Date", columns="Child", values="Pronunciation Accuracy (%)")
fig, ax = plt.subplots(figsize=(10, 6))
pivot_data.plot(kind="line", ax=ax, title="Pronunciation Accuracy Over Time", xlabel="Date", ylabel="Pronunciation Accuracy (%)")
st.pyplot(fig)

# Data Summary
st.subheader("Data Summary")
st.write(filtered_data.describe())

