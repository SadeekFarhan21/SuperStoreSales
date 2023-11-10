import pandas as pd
import plotly.express as px
import pandas as pd
import os
import warnings
import streamlit as st
import numpy as np

warnings.filterwarnings("ignore")

st.set_page_config(page_title='Superstore Sales Dasboard', page_icon=":bar_chart", layout = "wide")

st.title(':bar_chart: SuperStore Exploratory Data Analysis')
st.markdown('<style>div.block-container{padding-top: 1 rem;}</style>', unsafe_allow_html=True)

file = st.file_uploader(":file_folder: Upload your file ", type=['csv'])

if file is not None:
    file_name = file.name
    st.write(file_name)
    df = pd.read_csv(file_name)
else:
    current_directory = os.getcwd()
    os.chdir(current_directory)
    df = pd.read_excel('Superstore.xls')