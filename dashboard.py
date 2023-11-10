import pandas as pd
import plotly.express as px
import os
import warnings
import streamlit as st
import numpy as np

warnings.filterwarnings("ignore")

st.set_page_config(page_title='Superstore Sales Dashboard', page_icon=":bar_chart", layout="wide")

st.title(':bar_chart: SuperStore Exploratory Data Analysis')
st.markdown('<style>div.block-container{padding-top: 1rem;}</style>', unsafe_allow_html=True)

file = st.file_uploader(":file_folder: Upload your file", type=['csv'])
custom_name = st.text_input("Enter a custom name for the file (optional):")

if file is not None:
    if custom_name:
        file_name = custom_name + ".csv"
    else:
        file_name = file.name

    st.write(f"File Name: {file_name}")

    # Save the uploaded file
    with open(file_name, "wb") as f:
        f.write(file.getbuffer())

    st.success(f"File saved successfully: {file_name}")

    # Read the uploaded file into a DataFrame
    df = pd.read_csv(file_name)
else:
    df = pd.read_csv('Superstore.csv')

