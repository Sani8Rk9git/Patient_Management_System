import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def show_login():
    st.title("Doctor Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
    
        login_button = st.form_submit_button("Login")
    
        if login_button:
            response = requests.post(
                f"{API_URL}/login",
                json={
                    "username": username,
                    "password": password
                }
            )
    
            if response.status_code == 200:
                token = response.json()["access_token"]
                st.session_state["token"] = token
                st.session_state["page"] = "home"
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")

    st.divider()

    if st.button("Create a new account"):
        st.session_state["page"] = "register"
        st.rerun()