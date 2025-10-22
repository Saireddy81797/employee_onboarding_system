import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard(df):
    if df.empty:
        st.warning("No data available for analytics.")
        return
    
    st.metric("Total Employees", len(df))
    dept_counts = df["Department"].value_counts().reset_index()
    dept_counts.columns = ["Department", "Count"]

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Employees by Department")
        fig = px.bar(dept_counts, x="Department", y="Count", color="Department", title="Employees per Department")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Joining Trend")
        df["JoinDate"] = pd.to_datetime(df["JoinDate"])
        monthly = df.groupby(df["JoinDate"].dt.to_period("M")).size().reset_index(name="New Hires")
        fig2 = px.line(monthly, x="JoinDate", y="New Hires", markers=True, title="Monthly Hiring Trend")
        st.plotly_chart(fig2, use_container_width=True)
