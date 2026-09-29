import streamlit as st
import requests
import pandas as pd

def delete_record():
    st.subheader("Delete From record")
    if "token" not in st.session_state:
        st.warning("Please log in first to view patients.")
        return
        
    with st.form("delete_form"):
        p_id = st.number_input("Enter patient ID", min_value=1, step=1)
    
        submitted6 = st.form_submit_button("Delete it")
    
    if submitted6:
        response = requests.delete(f"http://127.0.0.1:8000/delete/{p_id}", headers={"Authorization": f"Bearer {st.session_state['token']}"})
    
        if response.status_code == 201:
                st.balloons()
                st.success("Patient deleted!!")
        else:
            st.error(response.text)