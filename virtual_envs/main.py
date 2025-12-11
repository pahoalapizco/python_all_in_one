from news_analizer.api_client import fetch_news
from news_analizer.config import API_KEY, AVAILABLE_LANGUAGES
from news_analizer.exceptions import APIKeyError


def get_query_lang_by_user():
    welcome_msg = "Bienvenid@ a tu portal de noticias favorito! 📰"
    query = input("¿Qué tema de noticias estas buscando?\n")
    lang_menu = f"""
¿En que idioma quieres leer las noticias sobre {query}?
(❗️Sino seleccionas un idioma recibiras las noticas en todos los idiomas disponibles.)
    """
    print(welcome_msg, lang_menu)

    for idx, language in enumerate(AVAILABLE_LANGUAGES.keys(), start=1):
        print(f"{idx} - {language}")

    lang = ""
    lang_opt = input("Selecciona el número correspondiente al idioma: ")

    if lang_opt.isdigit():
        lang_opt = int(lang_opt)
        if lang_opt > len(AVAILABLE_LANGUAGES):
            raise ValueError(
                f"Se esperaba un valor en el rango de 0 - {len(AVAILABLE_LANGUAGES)}, se obtuvo {lang_opt}."
            )

        lang = "" if lang_opt == 0 else list(AVAILABLE_LANGUAGES.values())[lang_opt - 1]
    else:
        raise ValueError(
            f"{lang_opt} no se encuentra dentro de las opciones disponibles."
        )
    return query, lang


if __name__ == "__main__":
    try:
        query, lang = get_query_lang_by_user()
        resp = fetch_news("newsapi", api_key=API_KEY, query=query, lang=lang)
        print("Articuloes totales: ", resp["totalResults"])
        print(resp["articles"])
    except ValueError as e:
        print(e)
    except APIKeyError as e:
        print(f"❌ Error: {e}")
