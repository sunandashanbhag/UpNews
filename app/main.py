from fastapi import FastAPI
from app.api.v1.endpoints import news, mood

# Setup FastAPI server
app = FastAPI(title="UpNews")

# Include routes
app.include_router(news.router, prefix="/api/v1/news", tags=["News"])
app.include_router(mood.router, prefix="/api/v1/mood", tags=["Mood"])