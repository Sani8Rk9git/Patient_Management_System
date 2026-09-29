import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"


def show_register():

    st.title("Doctor Registration")

    with st.form("register_form"):
        username = st.text_input("Choose Username")
        password = st.text_input("Choose Password", type="password")

        register_button = st.form_submit_button("Register")

        if register_button:
            response = requests.post(
                f"{API_URL}/register",
                json={
                    "username": username,
                    "password": password
                }
            )

            if response.status_code == 200:
                st.success("Registration successful! Please log in.")
            else:
                st.error("Registration failed. Username may already exist.")