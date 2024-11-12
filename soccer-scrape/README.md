# Web Scraping de Jugadores de Fútbol

Este proyecto implementa una aplicación de web scraping que extrae datos de futbolistas desde una página web específica utilizando BeautifulSoup. Los datos obtenidos se guardan en un archivo CSV para su posterior análisis, como estadísticas, nombres, posiciones y otros detalles relevantes de los jugadores.

## Estructura del Proyecto

- `config.py`: Contiene variables importantes para conectarnos a la página web.
- `scraper.py`: Contiene funciones que utilizan BeautifulSoup para navegar por el HTML de la página web y extraer los datos de los futbolistas..
- `csv-writer.py`: Se encarga de abrir un archivo CSV (si no existe, lo crea) y escribir los datos extraídos en él de manera organizada.
- `main.py`: Punto de entrada para ejecutar el menú interactivo.
