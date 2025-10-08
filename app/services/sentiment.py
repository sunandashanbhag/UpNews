# Sentiment analysis functions
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
import torch

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_trad(text):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "positive"
    elif score['compound'] <= -0.05:
        return "negative"
    return "neutral"

def get_sentiment_llm(text, mdl = 'finiteautomata/bertweet-base-sentiment-analysis'):
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="finiteautomata/bertweet-base-sentiment-analysis",
        device=0 if torch.cuda.is_available() else -1
    )
    result = sentiment_pipeline(text)[0]  # limit to 512 tokens
    print(result)
    return result["label"].lower()