import pandas as pd
import streamlit as st
import plotly.express as px


def app():
#    df = pd.read_excel("covid-19-dashboard_1-17-2021.xlsx")
    # st.write("This is mass data")
#    st.dataframe(df)
#    df = pd.read_excel("covid-19-dashboard_1-17-2021.xlsx", [0])
#    st.header("mass data")
    f = pd.ExcelFile("covid-19-dashboard_1-17-2021.xlsx")
    for i in f.sheet_names:
        df = pd.read_excel("covid-19-dashboard_1-17-2021.xlsx", i)
        st.dataframe(df)
