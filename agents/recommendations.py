def llm_recommendations(generate_summary, model, recommendation_prompt):
    """
    Generate recommendations based on extracted themes using a language model.

    Args:
        themes (list): List of extracted themes.
        model (str): The language model to use for generating recommendations.

    Returns:
        str: Generated recommendations.
    """
    combined_prompt = f"""{recommendation_prompt}\n\n here is the {generate_summary}"""
    model_response = model.generate_content(combined_prompt)
    return model_response.text

def generate_summary(feedback_df, prod_usage, merged_df):
    
    # 1. Sample customer feedback
    feedback_sample = feedback_df.head(50).to_string(index=False)
    # 2. Top themes identified
    top_themes = feedback_df['theme'].value_counts().head(5).to_string()
    # 3. Key product usage metrics
    usage_summary = prod_usage.describe().to_string()
    # 4. Correlations between feedback themes and product usage
    correlations = "correlation analysis not implemented"
    #correlations = merged_df.corr().to_string()

    # 5. Usage data stats
    usage_stats = prod_usage.describe().to_string()      
    # 6. Theme × Usage metrics (if you joined theme_id back to usage metrics)
    theme_usage = merged_df[['theme', 'feature_usage_count']].groupby('theme').mean().to_string()

    summary = f"""
    Sample Customer Feedback:
    {feedback_sample}
    Top Themes Identified:
    {top_themes}
    Key Product Usage Metrics:
    {usage_summary}
    Correlations Between Feedback Themes and Product Usage:
    {correlations}
    Usage Data Stats:
    {usage_stats}
    Theme × Usage Metrics:
    {theme_usage}
    """
    return summary