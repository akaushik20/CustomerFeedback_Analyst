# Customer Feedback Analyst

A Streamlit-based app that analyzes customer feedback, extracts key themes using LLMs, joins with product usage metrics, and provides actionable recommendations using LLM.

🔗 Hosted on [Streamlit Cloud](https://customerfeedbackanalyst-584hnbfdyx9jwkfascp2bh.streamlit.app/)
---

## ✨ Problem Framing & Assumptions

### Problem
Businesses receive qualitative customer feedback and quantitative product usage logs. Analyzing both together is essential but time-consuming.

**Goal**: Build an AI-powered system that:
- Extracts consistent, short themes from unstructured feedback.
- Quantifies trends in sentiment and theme frequency.
- Joins with product usage to surface data-backed insights.
- Outputs recommendations with rationale.

---

## ⚙️ Setup Instructions

### Requirements
- Python 3.9+
- Google Generative AI SDK (`google.generativeai`)
- Streamlit
- Install the requirements.txt to install all the required libraries 

### Installation
```bash
# Clone the repo
$ git clone https://github.com/akaushik20/CustomerFeedback_Analyst.git
$ cd CustomerFeedback_Analyst

# Set up virtual environment
$ python -m venv myenv
$ source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# Set up your Gemini API key
$ export GOOGLE_API_KEY=your_key_here  # Or set in Streamlit secrets

---

## 🚀 How to Run the App

### 1. Prepare Your Data
Ensure you have two files:
- `customer_feedback.csv`: With columns `id`, `customer_id`, `created_at`, `message`
- `product_usage.csv`: With relevant user activity or feature engagement

### 2. Launch the Streamlit App
```bash
streamlit run app.py
```

### 3. App Steps
1. **Load Data**: Parses feedback and product usage files.
2. **Extract Themes**: LLM analyzes feedback and returns themes with sentiment.
3. **Match Themes to Feedback**: Uses semantic similarity for tagging.
4. **Trend Graphs**: Visualizes theme frequency by week/month.
5. **Recommendations**: Gemini generates 4-5 insights using joined data.

---

## 📅 Key Decisions & Trade-offs
- Used a lightweight Streamlit front end for simplicity and ease of deployment. Hosting on Streamlit Cloud makes it straightforward to share with a broader audience.  
- Implemented LLM-based theme extraction. Large Language Models are well-suited for topic classification. Gemini was selected as the foundational model for its cost-effectiveness and quick response times.  
- Generated embeddings using the Sentence Transformer library and applied cosine similarity to link feedback to themes. Alternatives like FAISS or OpenAI embeddings are other options but not suitable for this use case given the simplicity of the sample dataset.  
- Summarized the data before including it in the final recommendation prompt, rather than passing all raw feedback. Supplying raw data could have introduced irrelevant or misleading context.  

## ⏳ What I'd Do Next
- Explore a multi-agent setup using LangGraph or CrewAI  
- Add memory to enhance continuity within the multi-agent workflow  
- Cache results once the LLM extracts themes from customer feedback (avoid re-running if results are already validated)  
- Perform deeper analysis on each theme by correlating product usage patterns with negative sentiment  
- Improve overall code structure through refactoring  

---
Hosted

Built by [Arpita Kaushik](https://github.com/akaushik20)