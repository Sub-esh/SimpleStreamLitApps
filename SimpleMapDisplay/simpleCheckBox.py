import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox("Display Data"):
    chartData = pd.DataFrame(
        np.random.randn(20,3),
        columns = ['a','b','c']
    )
    chartData