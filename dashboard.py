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
if file is not None:
    file_name = file.name

    st.write(f"File Name: {file_name}")

    # Save the uploaded file
    with open(file_name, "wb") as f:
        f.write(file.getbuffer())

    st.success(f"File saved successfully: {file_name}")

    # Read the uploaded file into a DataFrame
    df = pd.read_csv(file_name)
else:
    df = pd.read_excel('Superstore.xls')

col1, col2 = st.columns((2))
df['Order Date'] = pd.to_datetime(df['Order Date'])
start_date = pd.to_datetime(df["Order Date"]).min()
end_date = pd.to_datetime(df["Order Date"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", start_date))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", end_date))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

st.sidebar.header('Choose your filter: ')
region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

state = st.sidebar.multiselect("Pick the State", df2["State"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]

city = st.sidebar.multiselect("Pick the City",df3["City"].unique())