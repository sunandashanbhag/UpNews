import unittest
from app.services.news_service import fetch_latest_news
from dotenv import load_dotenv

load_dotenv()

class TestNewsService(unittest.TestCase):
    def test_fetch_news(self):
        articles = fetch_latest_news("science")
        self.assertIsInstance(articles, list)
        self.assertGreater(len(articles), 0)
        self.assertIn("title", articles[0])

if __name__ == '__main__':
    unittest.main()
