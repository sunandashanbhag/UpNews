from fastapi import APIRouter,HTTPException
from app.services.news_filter import get_mood_filtered_news

router = APIRouter()

@router.get("/{mood}")
def news_by_mood(mood: str):
    try:
        articles = get_mood_filtered_news(mood)
        return {"articles": articles}
    except Exception as e:
        print("Error occurred:", str(e))
        raise HTTPException(status_code=500, detail="Server error: " + str(e))
    # return {"message": "Mood endpoint working"}
