import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROD_USAGE_FILE_PATH = os.path.join(BASE_DIR, 'data\product_usage.csv')
FEEDBACK_FILE_PATH = os.path.join(BASE_DIR, 'data', 'feedback.jsonl')

THEME_EXTRACTION_PROMPT = """You are a theme extraction agent. 
Your task is to analyze customer feedback and extract the main themes or topics discussed. 
For each theme, provide a brief description and list relevant keywords."""

