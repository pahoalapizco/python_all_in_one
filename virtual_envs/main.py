import json
import sys
import urllib.error
import urllib.parse
import urllib.request  # configuración para hacer requests a apis

sys.stdout.reconfigure(encoding="utf-8")

API_KEY = ""
BASE_URL = "https://newsapi.org/v2/everything"


def news_client(api_key: str, query: str, timeout: int = 30, retries: int = 3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            print(f"NewsAPI: {query} con timeout {timeout}")
            return json.loads(data)

    except urllib.error.HTTPError as e:
        print(f"Error HTTP: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"Error de conexión/URL: {e.reason}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def guardian_client():
    pass


def fetch_news(api_name, *args, **kargs):
    base_config = {"timeout": 30, "retries": 3}
    config = {**base_config, **kargs}

    api_clients = {"newsapi": news_client, "guardian": guardian_client}
    client = api_clients[api_name]
    return client(*args, **config)


if __name__ == "__main__":
    resp = fetch_news("newsapi", api_key=API_KEY, query="Python")
    print(resp.keys())
