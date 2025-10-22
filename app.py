import streamlit as st
import pandas as pd
import uuid
import os

# File setup
DATA_FILE = "employee_data.csv"
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["EmployeeID", "Name", "Department", "Role", "Email", "JoinDate"])
    df.to_csv(DATA_FILE, index=False)

st.set_page_config(page_title="Employee Onboarding System", page_icon="👥", layout="wide")

st.title("👥 Employee Onboarding & Record Management System")
menu = ["Add Employee", "View Records", "Analytics"]
choice = st.sidebar.selectbox("Select Option", menu)

if choice == "Add Employee":
    st.subheader("Add New Employee Record")
    with st.form("add_form"):
        name = st.text_input("Full Name")
        dept = st.selectbox("Department", ["HR", "Engineering", "Finance", "Operations"])
        role = st.text_input("Role/Designation")
        email = st.text_input("Email")
        date = st.date_input("Joining Date")
        submitted = st.form_submit_button("Add Record")

        if submitted and name and email:
            emp_id = "EMP" + str(uuid.uuid4())[:8]
            new_data = pd.DataFrame([[emp_id, name, dept, role, email, date]],
                                    columns=["EmployeeID", "Name", "Department", "Role", "Email", "JoinDate"])
            df = pd.read_csv(DATA_FILE)
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success(f"✅ Employee {name} added successfully with ID: {emp_id}")

elif choice == "View Records":
    st.subheader("Employee Records")
    df = pd.read_csv(DATA_FILE)
    st.dataframe(df)

    search = st.text_input("Search by Name or Department")
    if search:
        filtered = df[df["Name"].str.contains(search, case=False) | df["Department"].str.contains(search, case=False)]
        st.dataframe(filtered)

elif choice == "Analytics":
    st.subheader("HR Analytics Dashboard")
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        st.warning("No data available yet.")
    else:
        dept_count = df["Department"].value_counts()
        st.bar_chart(dept_count)
        st.metric("Total Employees", len(df))
