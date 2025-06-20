import streamlit as slt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#title
slt.title("Streamlit App to Demonstrate Widget Functions")

#sidebar
slt.sidebar.header("Sidebar Options")

#text/number input
slt.subheader("Text Input")
slt.write("You Entered:",slt.text_input("Enter a text:"))
slt.subheader("Number Input")
slt.write("Number Input",slt.number_input("Number Input"))

#slider
slt.subheader("Slider")
age = slt.slider("Select you age",0,100,25)
slt.write("You are:", age, "Years old")

#Button
slt.subheader("Button")
if slt.button("Click Me"):
    slt.write("Button Clicked!")

#Radio Button
slt.subheader("Radio Button")
YourSelection = slt.radio("Make a selection:",["Choice1","Choice2","Choice3"])
slt.write("Your selection:",YourSelection)
