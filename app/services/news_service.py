# Fetch and process news
import requests
import os
from dotenv import load_dotenv
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_latest_news(query="general", language="en"):
    url = f"https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={NEWS_API_KEY}"
    print(url)
    response = requests.get(url)
    return response.json().get("articles", ["none"])
