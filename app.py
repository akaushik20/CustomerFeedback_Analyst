import streamlit as st
import pandas as pd
from agents.data_loader import DataLoader  # Import the class
from agents.theme_extractor_agent import extract_themes
from agents.analysis_agent import trend_analysis, data_summary
import config
from google import generativeai as genai

st.title("Customer Feedback Analyst")
bt_loadData=st.button("Load Data")

p_dataload=False
f_dataload=False
valid_json=False

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

if bt_loadData:
    loader = DataLoader()  # Create an instance
    
    prod_usage = loader.load_data(config.PROD_USAGE_FILE_PATH)  # Call a method (example)
    if prod_usage.empty:
        st.write("No data found in product usage file.")
    else:
        st.write("Product Usage Data loaded successfully!")
        p_dataload = True

    feedback = loader.load_json(config.FEEDBACK_FILE_PATH)
    if feedback.empty:
        st.write("No data found in feedback file.")
    else:
        st.write("Feedback Data loaded successfully!")
        f_dataload = True
        st.session_state["feedback"] = feedback

if p_dataload and f_dataload:
    print("Extracting themes...")
    themes, valid_json = extract_themes(feedback, config.THEME_EXTRACTION_PROMPT, 
                            model=model, prod_usage=None)
    st.session_state["themes"] = themes
    st.session_state["valid_json"] = valid_json
    st.write("Extracted Themes:")
    if valid_json:
        st.write("Successfully extracted valid JSON themes.")
    else:
        st.write("The extracted themes are not valid JSON.")

if st.session_state.get("valid_json", False):
    bt_analytics=st.button("Show Analytics !")

    if bt_analytics:
        data_summary_df = data_summary(config.FEEDBACK_FILE_PATH, "genai_response.json")
        #trend_analysis_response = trend_analysis(st.session_state["themes"],
        #                                          st.session_state["feedback"],
        #                                            config.TREND_ANALYSIS_PROMPT, model)
        st.write(f'Data Summary with {len(data_summary_df)} records')
        #st.write(trend_analysis_response.text)







