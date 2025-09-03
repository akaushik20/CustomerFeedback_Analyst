import streamlit as st
from google import generativeai as genai
import json


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

