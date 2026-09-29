import streamlit as st


st.set_page_config(page_title="Patient Management System",initial_sidebar_state="collapsed",layout="wide")

from create import front_create
from view import view_all, view_one, view_sort
from update import update_record
from delete import delete_record
from login import show_login
from register import show_register

if "page" not in st.session_state:
    st.session_state.page = "home"


st.title("Patient Management App")



#callback function
def navigate_to(page):
    st.session_state.page = page

def home_page():
    st.title("Manage Your Patients")
    st.write("")
    st.write("")
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True):
            st.subheader("Create Patient record")
            st.button("Create", use_container_width=True, on_click=navigate_to, args=("create",))

    with col2:
        with st.container(border=True):
            st.subheader("View Patients")
            st.button("View", use_container_width=True, on_click=navigate_to, args=("view",))

    with col3:
        with st.container(border=True):
            st.subheader("Update Patient Record")
            st.button("Update", use_container_width=True, on_click=navigate_to, args=("update",))

    with col4:
        with st.container(border=True):
            st.subheader("Delete Patient Record")
            st.button("Delete", use_container_width=True, on_click=navigate_to, args=("delete",))

    
    st.button("Login",on_click=navigate_to, args=("login",))

    st.button("Register",on_click=navigate_to, args=("register",))

    if st.button("Logout"):
        st.session_state.pop("token",None)
        st.session_state["page"] = "home"
        # st.balloons()
        st.rerun()
    


if st.session_state.page == "home":
    home_page()

elif st.session_state.page == "create":
    front_create()
    st.button("Back to Home", on_click=navigate_to, args=("home",))

elif st.session_state.page == "view":
    if "view_option" not in st.session_state:
        st.session_state.view_option = None

    def go_to(view_option):
        st.session_state.view_option = view_option

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("See all records", on_click=go_to, args=("see_all",))
    with col2:
        st.button("See one record", on_click=go_to, args=("see_one",))
    with col3:
        st.button("Sort records and see", on_click=go_to, args=("sort_see",))

    if st.session_state.view_option == "see_all":
        view_all()
    elif st.session_state.view_option == "see_one":
        view_one()
    elif st.session_state.view_option == "sort_see":
        view_sort()

    st.button("Back to Home", on_click=navigate_to, args=("home",))

elif st.session_state.page == "update":
    update_record()
    st.button("Back to Home", on_click=navigate_to, args=("home",))

elif st.session_state.page == "delete":
    delete_record()
    st.button("Back to Home", on_click=navigate_to, args=("home",))

elif st.session_state.page == "login":
    show_login()
    st.button("Back to Home", on_click=navigate_to, args=("home",))


elif st.session_state.page == "register":
    show_register()
    st.button("Back to Home", on_click=navigate_to, args=("home",))