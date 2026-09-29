import streamlit as st
import requests
import pandas as pd


def front_create():
    st.subheader("Create New patient")
    if "token" not in st.session_state:
        st.warning("Please log in first to view patients.")
        return
    
    with st.form("create_form"):
        p_id = st.number_input("Enter Patient ID:", min_value=1, step=1)
        name = st.text_input("Enter Patient Name:")
        city = st.text_input("Enter Patient City:")
        age = st.number_input("Enter Patient Age:", min_value=1, step=1)
        gender = st.selectbox("Select Gender of Patient", ["male","female","others"])
        height = st.number_input("Enter the height of the patient in meters")
        weight = st.number_input("Enter the weight of the patient in kg")
    
        submitted1 = st.form_submit_button("Create Patient")
    
    if submitted1:
        patient_data = {
            "p_id": p_id,
            "name": name,
            "city": city,
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight
        }
    
        response = requests.post("http://127.0.0.1:8000/create", json=patient_data, headers={"Authorization": f"Bearer {st.session_state['token']}"})
    
        if response.status_code == 201:
            st.balloons()
            st.success("Patient Created!!")
        else:
            st.error(response.text)