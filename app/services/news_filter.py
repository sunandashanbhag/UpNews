from .news_service import fetch_latest_news
from app.services.sentiment import get_sentiment_llm, get_sentiment_trad
from .summarize_news import summarize

def get_mood_filtered_news(user_mood):
    all_news = fetch_latest_news()
    filtered_news = []

    for article in all_news:
        title = article.get("title", "")
        content = article.get("content") or article.get("description", "") or ""
        sentiment = get_sentiment_llm(title + "- " + content)

        if sentiment == user_mood.lower():
            summary = summarize(content)
            article["summary"] = summary
            article["sentiment"] = sentiment
            filtered_news.append(article)
    print(filtered_news[0]['content'])
    return filtered_news

    # [article for article in all_news
            # if get_sentiment_llm(article.get("content", "")) == user_mood]
