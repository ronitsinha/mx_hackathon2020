import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache
def get_data(option):
    if option == 1:
        return pd.read_csv("http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv")
    elif option == 2:
        return pd.read_csv("http://data.insideairbnb.com/united-states/ma/boston/2020-11-10/visualisations/listings.csv")

def get_availability(df, show_exp, neighborhood):
    return df.query(f"""neighbourhood_group==@neighborhood{show_exp}\
        and availability_365>0""").availability_365.describe(\
            percentiles=[.1, .25, .5, .75, .9, .99]).to_frame().T

def display_dataset(option):
    if option == 0:
        return
    df = get_data(option)
    st.header("Airbnb listings: data at a glance")
    st.dataframe(df.head())

    st.write("Using a radio button restricts selection to only one option at a time.")
    neighborhood = st.radio("Neighborhood", df.neighbourhood_group.unique())
    show_exp = st.checkbox("Include expensive listings")
    show_exp = " and price<200" if not show_exp else ""
    st.table(get_availability(df, show_exp, neighborhood))

def app():
    col1, col2 = st.beta_columns([1, 4])

    with col1:
        display = ("please choose a city", "new york", "boston")

        options = list(range(len(display)))

        value = st.selectbox("city", options, format_func=lambda x: display[x])

    with col2:
        display_dataset(value)

