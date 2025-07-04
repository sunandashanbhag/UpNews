import os

folders = [
    "app/api/v1/endpoints",
    "app/core",
    "app/services",
    "app/models",
    "app/db",
    "app/utils",
    "tests"
]

files = {
    "app/main.py": "",
    "app/api/__init__.py": "",
    "app/api/v1/__init__.py": "",
    "app/api/v1/endpoints/__init__.py": "",
    "app/core/config.py": "# Configuration goes here",
    "app/services/news_service.py": "# Fetch and process news",
    "app/services/sentiment.py": "# Sentiment analysis functions",
    "app/models/news.py": "",
    "app/models/mood.py": "",
    "app/models/user.py": "",
    "app/db/session.py": "",
    "app/db/crud.py": "",
    "app/utils/logger.py": "",
    "tests/test_news.py": "",
    "tests/test_mood.py": "",
    ".env": "# Environment variables",
    "requirements.txt": "# Dependencies",
    "Dockerfile": "# Docker container config",
    "docker-compose.yml": "",
    "README.md": "# MoodFeed - Mood-Based News App",
    ".gitignore": "*.pyc\n__pycache__/\n.env\n"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Folder structure created successfully!")
