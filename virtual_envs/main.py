from news_analizer.api_client import fetch_news
from news_analizer.config import API_KEY
from news_analizer.exceptions import APIKeyError

if __name__ == "__main__":
    try:
        resp = fetch_news("newsapi", api_key=API_KEY, query="Python")
        print(resp.keys())
    except APIKeyError as e:
        print(f"❌ Error: {e}")
