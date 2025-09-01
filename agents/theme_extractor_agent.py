import streamlit as st
from google import generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
system_prompt = """You are a theme extraction agent. Your task is to analyze customer feedback and extract the main themes or topics discussed. 
For each theme, provide a brief description and list relevant keywords."""

def extract_themes():
    genai_response = model.generate_content(system_prompt)
    print(genai_response.text)
    return genai_response.text

#if __name__ == "__main__":
#    extract_themes()