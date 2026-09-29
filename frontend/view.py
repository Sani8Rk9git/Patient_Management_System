import streamlit as st
import requests
import pandas as pd

def view_all():
    st.subheader("View Patients")
    if "token" not in st.session_state:
        st.warning("Please log in first to view patients.")
        return
    
    with st.form("view form"):
        st.write("Want to see all Patients??")
        submitted2 = st.form_submit_button("Yes All")

    if submitted2:
        response = requests.get("http://127.0.0.1:8000/view", headers={"Authorization": f"Bearer {st.session_state['token']}"})
        if response.status_code == 200:
            data = response.json()
            st.dataframe(data)
        else:
            st.warning("Please log in first!!")

def view_one():
    st.subheader("View a single patient")
    if "token" not in st.session_state:
        st.warning("Please log in first to view patients.")
        return

    
    with st.form("view_one form"):
        p_id = st.number_input("Enter Patient ID:", min_value=1, step=1)
        submitted3 = st.form_submit_button("Get the Patient")

    if submitted3:
        response = requests.get(f"http://127.0.0.1:8000/view/{p_id}", headers={"Authorization": f"Bearer {st.session_state['token']}"})
        if response.status_code == 200:
            data = response.json()
            st.dataframe(data)

def view_sort():
    st.subheader("View Patients in sorted order")
    if "token" not in st.session_state:
        st.warning("Please log in first to view patients.")
        return
        
    with st.form("view_sort"):
        st.write("Select the column to sort according to it.")
        col_name = st.selectbox("Choose Column:",["height","weight","age","city","name","verdict"])
        order = st.selectbox("Choose Order of sorting:",["asc","desc"])
        submitted4 = st.form_submit_button("Lets get it")

    if submitted4:
        response = requests.get(f"http://127.0.0.1:8000/sort?sort_by={col_name}&order={order}", headers={"Authorization": f"Bearer {st.session_state['token']}"})
        if response.status_code == 200:
            data = response.json()
            st.dataframe(data)