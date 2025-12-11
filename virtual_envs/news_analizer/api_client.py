import json
import urllib.error
import urllib.parse
import urllib.request  # configuración para hacer requests a apis
from typing import Any

from .config import BASE_URL
from .exceptions import APIKeyError


def validate_api_key(api_key: str) -> bool:
    """Valida que la api key tenga un formato valido.

    Args:
        api_key (str): Valor de la api key a validar

    Returns:
        bool: True si la api key es valida, False en caso contrario
    """
    return len(api_key) > 10 and api_key.isalnum()


def news_client(api_key: str, query: str, timeout: int = 30, retries: int = 3) -> dict:
    """Llamada a la API de news api

    Args:
        api_key (str): Api key requerida para la API de news api,
        query (str): Término de la busquéda
        timeout (int, optional): Tiempo máximo de respuesta. Defaults to 30.
        retries (int, optional): Número de reintentos en caso de fallo. Defaults to 3.

    Raises:
        APIKeyError: Error en el formato de la API KEY

    Returns:
        dict: Datos de la respuesta en formato JSON, estructura:
        {
            "status": "",
            "totalResults": 0,
            "articles": [{}]
        }
    """
    if not validate_api_key(api_key):
        raise APIKeyError("API_KEY no tiene el formato correcto.")

    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    resp: dict = dict()
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            print(f"NewsAPI: {query} con timeout {timeout}")
            resp = json.loads(data)

    except urllib.error.HTTPError as e:
        print(f"Error HTTP: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"Error de conexión/URL: {e.reason}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        return resp


def fetch_news(api_name: str, *args: Any, **kargs: Any) -> dict[str, Any]:
    """Función que recibe el nombre de la API y sus parámetros, y llama al cliente correspondiente.

    Args:
        api_name (str): Nombre de la API a utilizar ("newsapi")

    Returns:
        dict[str, Any]: Datos de la respuesta de la API en formato JSON
    """
    base_config: dict[str, int] = {"timeout": 30, "retries": 3}
    config: Any = {**base_config, **kargs}

    api_clients: dict[str, Any] = {"newsapi": news_client}
    client = api_clients[api_name]
    resp = client(*args, **config)
    return resp


if __name__ == "__main__":
    pass
