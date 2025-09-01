import streamlit as st
import pandas as pd
from agents.data_loader import DataLoader  # Import the class
import config

st.title("Customer Feedback Analyst")
bt_loadData=st.button("Load Data")

if bt_loadData:
    loader = DataLoader()  # Create an instance
    
    prod_usage = loader.load_data(config.PROD_USAGE_FILE_PATH)  # Call a method (example)
    if prod_usage.empty:
        st.write("No data found in product usage file.")
    else:
        st.write("Product Usage Data loaded successfully!")

    feedback = loader.load_json(config.FEEDBACK_FILE_PATH)
    if feedback.empty:
        st.write("No data found in feedback file.")
    else:
        st.write("Feedback Data loaded successfully!")







