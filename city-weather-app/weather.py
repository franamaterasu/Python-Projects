import requests
import os

# Clave de API cargada desde una variable de entorno para acceder a los datos del clima
API_KEY = os.getenv("API_KEY", "7a68b98b464faf27752d6128b275674a")


def get_weather_data(city):
    """
    Realiza una solicitud a la API de clima y devuelve los datos en formato JSON.

    Parámetros:
    city(str): Nombre de la ciudad para consultar el clima

    Retorna:
    dict o None: Datos del clima de la ciudad en formato JSON si la solicitud ha ido correctamente, None si ha ocurrido algún error
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)

        response.raise_for_status()  # Lanza una excepción para errores HTTP

        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")

    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")

    except requests.exceptions.Timeout as timeout_err:
        print(f"Error de timeout: {timeout_err}")

    except requests.exceptions.RequestException as req_err:
        print(f"Error al obtener los datos de la API: {req_err}")
    return None


def parse_weather_data(data):
    """
    Extrae y valida la información del clima del JSON de respuesta.

    Parámetros:
    data(dict): Datos del clima de la ciudad en formato JSON obtenidos desde la API

    Retorna:
    dict: Diccionario con los datos del clima de la ciudad
    """

    weather_data = {}

    # Obtenemos el nombre de la ciudad
    if "name" in data:
        weather_data["city"] = data["name"]
    else:
        weather_data["city"] = "Not available"

    # Obtenemos el pais de la ciudad
    if "sys" in data:
        weather_data["country"] = data["sys"]["country"]
    else:
        weather_data["country"] = "Not available"

    # Obtenemos la información del clima
    if "weather" in data and len(data["weather"]) > 0:
        weather_data["main"] = data["weather"][0]["main"]
        weather_data["description"] = data["weather"][0]["description"]
    else:
        weather_data["main"] = "Not available"
        weather_data["description"] = "Not available"

    # Obtenemos la temperatura y la humedad
    if "main" in data:
        weather_data["temperature"] = f'{data["main"]["temp"]}ºC'
        weather_data["humidity"] = data["main"]["humidity"]
    else:
        weather_data["temperature"] = "Not available"
        weather_data["humidity"] = "Not available"

    # Obtenemos la velocidad del viento
    if "wind" in data:
        weather_data["windspeed"] = data["wind"]["speed"]
    else:
        weather_data["windspeed"] = "Not available"

    return weather_data
