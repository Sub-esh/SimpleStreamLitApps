import streamlit as slt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#title
set.title("Streamlit App to Demonstrate Widget Functions")
#sidebar
set.sidebar.header("Sidebar Options")
#text/number input
st.subheader("Text Input")
st.write("You Entered:",st.text_input("Enter a text:"))
