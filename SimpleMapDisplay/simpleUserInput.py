import streamlit as st

st.text_input("Enter your name", key= "name")
st.session_state.name