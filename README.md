### 📊 HR Analytics Dashboard built using Streamlit & Python  

---

## 🌐 Live Demo  
👉 **[Click here to view the live app](https://saireddy81797-employee-onboarding-system-app-htdbmh.streamlit.app/)**  

---

## 🧩 Project Overview  

The **Employee Onboarding & Record Management System** is a **Streamlit-based web application** that helps HR teams manage employee data, onboarding records, and department-level analytics in one unified dashboard.  

This project was built to simulate a **Human Resource Information System (HRIS)** — similar to the systems used at **Rippling**, where employee data serves as the backbone of workforce management.  

The app allows HR departments to:  
- Add, view, and update employee information.  
- Upload and organize onboarding documents.  
- Generate real-time analytics dashboards showing employee distribution by department.  
- Simplify data validation, storage, and visualization in one place.  

---

## 🛠️ Features  

✅ **Add Employee Records** – Input new employees with ID, department, email, and role.  
✅ **View All Records** – Tabular view of all employee data with sorting and search.  
✅ **Upload Documents** – Upload offer letters, ID proofs, resumes, and joining forms (stored in `/assets/sample_docs`).  
✅ **Analytics Dashboard** – Visualize number of employees per department.  
✅ **Auto Data Validation** – Ensures correct email format and valid joining date.  
✅ **Lightweight Deployment** – Fully deployable using Streamlit Cloud with zero backend setup.  

---
💼 Relevance to Rippling’s HRIS Internship

This project directly aligns with Rippling’s HRIS team objectives, focusing on:

Managing employee records (hiring, onboarding, offboarding).

Ensuring data correctness and completeness across the organization.

Creating a unified platform that integrates HR, IT, and Finance data.

Building scalable, data-driven automation tools for internal teams.

By completing this project, I demonstrated:

End-to-end ownership of a data management product.

Application of software engineering principles to real-world HR problems.

Ability to build full workflows using modern tools like Streamlit and Python.

---

## 📁 Folder Structure  

# employee_onboarding_system
## 📁 Folder Structure  

employee_onboarding_system/
│
├── app.py # Main Streamlit application
├── employee_data.csv # Employee data (30 sample rows)
├── requirements.txt # Required dependencies
│
├── assets/
│ ├── logo.png # App logo
│ └── sample_docs/ # Sample uploaded PDFs
│ ├── offer_letter_sample.pdf
│ ├── id_proof_sample.pdf
│ ├── resume_sample.pdf
│ └── joining_form_sample.pdf
│
└── utils/
├── database.py # Functions for data storage/retrieval
├── analytics.py # HR dashboard visualizations
└── validation.py # Input validation (email, date, etc.)

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app locally
streamlit run app.py

4️⃣ Deploy on Streamlit Cloud

Push your repo to GitHub.

Visit https://share.streamlit.io
.

Connect your GitHub repo and deploy.

Your live app will be hosted instantly. 🎉


