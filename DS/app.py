import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, state, mass, cdc, massgov

app = MultiApp()


app.add_app("Home", home.app)
app.add_app("Massachusetts", massgov.app)
app.add_app("United States", cdc.app)
app.add_app("Global", mass.app)

# main app
app.run()