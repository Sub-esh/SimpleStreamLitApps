import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'column1' : [1,2,3,4,5],
    'column2' : [11,22,33,44,55]
})

userChoice = st.selectbox(
    "Which number would you like to select",
    df['column1']
)

st.write("You chose:",userChoice)