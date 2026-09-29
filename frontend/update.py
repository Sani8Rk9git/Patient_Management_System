import streamlit as st
import requests
import pandas as pd

def update_record():
    st.subheader("Update Patient Record")
    if "token" not in st.session_state:
        st.warning("Please log in first to view patients.")
        return
        
    with st.form("update_form"):
        st.write("Enter Patient ID and the Fields that you want to update")
        p_id = st.number_input("Enter patient ID:", min_value=1, step=1)
    
        name = st.text_input("Enter patient name:")
        city = st.text_input("Enter patient city:")
    
        age = st.number_input("Enter Patient age:", min_value=1, value=None)
        gender = st.selectbox("Select Gender of patient", ["Not selected","male","female","others"])
        height = st.number_input("Enter the height of the patient in meters", value=None)
        weight = st.number_input("Enter the weight of the patient in kg",value=None)
    
        submitted5 = st.form_submit_button("Update Patient")
    
    if submitted5:
        patient_data = {}
    
        if name:
            patient_data["name"] = name
        if city:
            patient_data["city"] = city
        if age is not None:
            patient_data["age"] = age
        if gender != "Not selected":
            patient_data["gender"] = gender
        if height is not None:
            patient_data["height"] = height
        if weight is not None:
            patient_data["weight"] = weight
        if not patient_data:
            st.warning("Please enter at least one field to update.")
    
        else:
            response = requests.put(f"http://127.0.0.1:8000/edit/{p_id}", json=patient_data, headers={"Authorization": f"Bearer {st.session_state['token']}"})
    
            if response.status_code == 201:
                st.balloons()
                st.success("Patient Updated!!")
            else:
                st.error(response.text)