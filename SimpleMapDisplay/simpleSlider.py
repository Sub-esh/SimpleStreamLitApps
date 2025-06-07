import streamlit as st

a = st.slider('slider value')
st.write(a, 'squared is', a*a)