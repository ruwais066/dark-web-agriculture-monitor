import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Agri-Shield Dark Web Monitor", layout="wide")

def login():
    st.title("🛡️ Secure Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "agri123":
            st.session_state["logged_in"] = True
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid Username or Password")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    st.sidebar.title("🛡️ Dashboard Menu")
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()

    app_mode = st.sidebar.selectbox("Navigate To", ["Monitor Home", "Global Threat Analysis", "Project Documentation"])

    keywords = [
        "farm database", "agriculture hack", "crop data leak", 
        "farm iot breach", "agriculture credentials"
    ]

    if app_mode == "Monitor Home":
        st.title("🌱 Agriculture Dark Web Monitoring System")
        st.write("Real-time Scanning for Agricultural Asset Vulnerabilities")
        
        user_input = st.text_area("Log Input:", height=200)
        
        if st.button("Initiate AI Scan"):
            if user_input:
                text = user_input.lower()
                found_threats = [word for word in keywords if word in text]
                
                if found_threats:
                    st.error(f"🚨 {len(found_threats)} Critical Threats Detected!")
                    chart_data = pd.DataFrame({
                        'Threat Found': found_threats,
                        'Severity Level': [9, 8, 7, 10, 6][:len(found_threats)]
                    })
                    fig = px.bar(chart_data, x='Threat Found', y='Severity Level', title="Threat Analysis")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.success("✅ SCAN CLEAN: No threats detected.")

    elif app_mode == "Global Threat Analysis":
        st.header("📊 Global Threat Statistics")
        stats_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar'], 'Attacks': [45, 62, 89]})
        fig2 = px.line(stats_data, x='Month', y='Attacks', title="Monthly Attack Trends")
        st.plotly_chart(fig2, use_container_width=True)

    elif app_mode == "Project Documentation":
        st.header("ℹ️ Project Information")
        st.write("This tool is designed to monitor dark web leaks for the agriculture sector.")