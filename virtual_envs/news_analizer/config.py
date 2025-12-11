import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"
AVAILABLE_LANGUAGES = {
    "Árabe": "ar",
    "Alemán": "de",
    "Inglés": "en",
    "Español": "es",
    "Francés": "fr",
    "Hebreo": "he",
    "Italiano": "it",
    "Neerlandés": "nl",
    "Noruego": "no",
    "Portugués": "pt",
    "Ruso": "ru",
    "Sueco": "sv",
    "Chino": "zh",
}
