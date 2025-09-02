import os
import streamlit as st
from google import generativeai as genai
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import altair as alt




def trend_analysis(themes, feedback, trend_prompt, model):
    #st.header("Trend Analysis")
    #st.write("This section will analyze trends over time based on the extracted themes.")
    # Placeholder for trend analysis logic
    combined_prompt = f"""{trend_prompt}.
    \n\nThemes:\n{json.dumps(themes, indent=2)}\n\nFeedback Data:\n{feedback.to_json(orient='records', lines=True)}"""

    analysis_response = model.generate_content(combined_prompt)

    return analysis_response

    #st.write("Trend analysis functionality is under development.")

def data_summary(feedback_path, genai_response_path):
    
    # Prepare Data
    # Load feedback
    feedback_df = pd.read_json(feedback_path, lines=True)
    print(feedback_df)

    # Load theme JSON
    with open(genai_response_path) as f:
        themes = json.load(f)

    # Combine theme + explanation for better context
    theme_texts = [f"{t['theme']}. {t['explanation']}" for t in themes]
    print(theme_texts)

    # Create embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')
    theme_embeddings = model.encode(theme_texts)
    feedback_embeddings = model.encode(feedback_df['message'].tolist())

    # Shape: (num_feedback, num_themes)
    similarity_matrix = cosine_similarity(feedback_embeddings, theme_embeddings)

    # Get best matching theme index per feedback
    best_theme_indices = similarity_matrix.argmax(axis=1)
    best_scores = similarity_matrix.max(axis=1)

    # Add matches back into DataFrame
    feedback_df["theme_id"] = [themes[i]["id"] for i in best_theme_indices]
    feedback_df["theme"] = [themes[i]["theme"] for i in best_theme_indices]
    feedback_df["sentiment"] = [themes[i]["sentiment"] for i in best_theme_indices]
    feedback_df["explanation"] = [themes[i]["explanation"] for i in best_theme_indices]
    feedback_df["confidence"] = best_scores.round(3)

    # Save output
    feedback_df.to_json("feedback_with_themes_embedded.json", orient="records", indent=4)

    return feedback_df

def plot_graphs(feedback_df):
    st.header("Data Visualizations")
    st.write("This section will contain various data visualizations based on the feedback data.")

    # Bar chart of theme distribution
    if "theme" in feedback_df.columns:
        theme_counts = feedback_df['theme'].value_counts().sort_values(ascending=False)
        #st.subheader("Theme Distribution")
        #st.bar_chart(theme_counts)
        theme_counts_df = theme_counts.reset_index()
        theme_counts_df.columns = ['theme', 'count']
        theme_counts_df = theme_counts_df.sort_values('count', ascending=False)
        st.subheader("Theme Distribution")
        st.bar_chart(theme_counts_df.set_index('theme'))
    else:
        st.write("No themes found in the feedback data to plot.")
    
    # Trend by week & month
    if "created_at" in feedback_df.columns:
        feedback_df["created_at"] = pd.to_datetime(feedback_df["created_at"])
        
        # Weekly trend
        feedback_df["week"] = feedback_df["created_at"].dt.to_period("W").apply(lambda r: r.start_time)
        weekly_trend = feedback_df.groupby("week").size()
        st.subheader("Feedback Trend by Week")
        st.line_chart(weekly_trend)

        # Monthly trend
        #feedback_df["month"] = feedback_df["created_at"].dt.to_period("M").apply(lambda r: r.start_time)
        #monthly_trend = feedback_df.groupby("month").size()
        #st.subheader("Feedback Trend by Month")
        #st.line_chart(monthly_trend)
    else:
        st.write("No date column found for trend analysis.")

