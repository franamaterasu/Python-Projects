from modules.scraper import obtener_soup, obtener_jugadores
from modules.csv_writer import guardar_jugadores_csv
from modules.config import URL, HEADERS

def main():
    soup = obtener_soup(URL, HEADERS)
    if soup:
        jugadores = obtener_jugadores(soup)
        guardar_jugadores_csv(jugadores)
    else:
        print("No se pudo obtener el contenido de la página.")

if __name__ == '__main__':
    main()
