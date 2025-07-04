from fastapi import APIRouter
from app.services.news_service import fetch_latest_news
import os

router = APIRouter()

@router.get("/debug/env")
def debug_env():
    return {"NEWS_API_KEY": os.getenv("NEWS_API_KEY")}

@router.get("/raw")
def get_news():
    return fetch_latest_news()
