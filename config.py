import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROD_USAGE_FILE_PATH = os.path.join(BASE_DIR, 'data\product_usage.csv')
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