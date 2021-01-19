import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table
from apps import massgov, cdc

def app():
    st.title('Home')

    st.write("COVID-19 DATA")


    st.dataframe(massgov.display_home(massgov.get_data()))
    st.write('Navigate to `Massachusetts` page to visualize the data')
    st.dataframe(cdc.display_home(cdc.get_data()))
    st.write('Navigate to `United States` page to visualize the data')
    # replace later
    st.markdown("### Sample Data")
    df = create_table()
    st.write(df)
    st.write('Navigate to `Global` page to visualize the data')



