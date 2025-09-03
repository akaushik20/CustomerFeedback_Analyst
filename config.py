import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#PROD_USAGE_FILE_PATH = os.path.join(BASE_DIR, 'data\product_usage.csv')
PROD_USAGE_FILE_PATH = "https://raw.githubusercontent.com/akaushik20/CustomerFeedback_Analyst/refs/heads/main/data/product_usage.csv"
FEEDBACK_FILE_PATH = os.path.join(BASE_DIR, 'data', 'feedback.jsonl')

#THEME_EXTRACTION_PROMPT = """You are a theme extraction agent. 
#Your task is to analyze customer feedback and extract the main themes or topics discussed. 
#For each theme, provide a brief description and list relevant keywords."""

THEME_EXTRACTION_PROMPT = """Role: You are a theme extraction agent. 
Task: Your task is to analyze customer feedback and extract the main themes or topics discussed.
 Given a batch of customer feedback messages,
    produce a JSON array where each item is:
    {
      "id": <string>,
      "theme": <<=5 words, concise, consistent>,
      "sentiment": <one of: negative|neutral|positive>,
      "explanation": <one sentence>,
      "confidence": <0..1>
    }
    - Keep theme vocabulary stable across the batch when similar.
    - Prefer business-relevant labels (e.g., "Chime linking errors", "Approval criteria confusion").
    - Ensure themes are distinct and non-overlapping.
    - Make sure the output is valid json and parsable.
    - Do not include any text before or after the JSON array. The output should be only valid JSON array.
    - If feedback is empty, return an empty list."""

TREND_ANALYSIS_PROMPT = """You are a trend analysis agent.
Your task is to analyze trends over time based on the extracted themes from customer feedback.
Given a list of themes and their associated feedback data, identify any emerging trends or patterns.
Plot how frequently these themes occur over time (weekly or monthly).
Include a short summary."""

RECOMMEDATION_AGENT = """
Role: You are an expert Customer Insights & Trend Analysis Agent, skilled at interpreting patterns in customer feedback and product usage data to drive actionable business decisions.

Task: 
Using the following three datasets:
1. Customer Feedback - includes customer messages, timestamps, theme of the feedback, sentiment of feedback and IDs  
2. Product Usage Data - contains metrics of customer interaction with product features  
3. Joined Dataset - combines feedback and usage per customer

You must:
- Identify 4 to 5 actionable recommendations
- For each recommendation, include a detailed rationale
- Support your rationale with observed trends, frequencies, and relevant data patterns
- Highlight customer pain points, opportunities, or product improvement ideas
- Avoid generic suggestions — focus on specific, data-backed insights

Instruction: 
Use all three datasets in context. Refer to trends over time, repeated themes, or correlations between feature usage and customer sentiment. Be concise, analytical, and outcome-driven.
"""