import streamlit as st
from google import generativeai as genai
import json

##api_key = st.secrets["GOOGLE_API_KEY"]
##genai.configure(api_key=api_key)
##model = genai.GenerativeModel("gemini-1.5-flash")

#system_prompt = """You are a theme extraction agent. Your task is to analyze customer feedback and extract the main themes or topics discussed. 
#For each theme, provide a brief description and list relevant keywords."""

def extract_themes(feedback_text, system_prompt, model, prod_usage=None):
    combined_prompt = f"{system_prompt}\n\nCustomer Feedback:\n{feedback_text}"
    print("Combined Prompt:", combined_prompt)  # Debugging line to check the prompt

    genai_response = model.generate_content(combined_prompt)
    text = genai_response.text.strip()

    if text.startswith("```json"):
        text = text[7:]  # remove ```json
    if text.startswith("```"):
        text = text[3:]  # fallback if just ```
    if text.endswith("```"):
        text = text[:-3]

    valid_json = True
    try:
        themes_json=json.loads(text[text.find("[") : text.rfind("]") + 1])
        valid_json = True
    except json.JSONDecodeError:
        print("The output is not valid JSON.")
        #themes_json = json.loads(text[text.find("[") : text.rfind("]") + 1])
        themes_json={"raw_output": text}
        valid_json = False 

    # save file 
    with open("genai_response.json", "w") as f:
        json.dump(themes_json, f, indent=4)
    #print(genai_response.text)
    return themes_json, valid_json

