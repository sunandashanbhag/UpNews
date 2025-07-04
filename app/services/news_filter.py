from .news_service import fetch_latest_news
from app.services.sentiment import get_sentiment

def get_mood_filtered_news(user_mood):
    all_news = fetch_latest_news()
    return [article for article in all_news
            if get_sentiment(article.get("title", "")) == user_mood]
