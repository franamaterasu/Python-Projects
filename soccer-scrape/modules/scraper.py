import requests
from bs4 import BeautifulSoup

def obtener_contenido(url, headers):
    # Realiza la solicitud HTTP y obtiene el contenido de la página
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f'Error al realizar la solicitud: {e}')
        return None

def obtener_soup(url, headers):
    # Obtiene el objeto BeautifulSoup a partir de la URL
    contenido = obtener_contenido(url, headers)
    if contenido:
        return BeautifulSoup(contenido, 'html.parser')
    return None


def obtener_jugadores(soup):
    # Procesa el contenido HTML para extraer la información de los jugadores
    jugadores = []
    
    players_table = soup.find_all('tr', class_=['odd', 'even'])

    for player in players_table:
        jugador = {
            "imagen": player.select('.inline-table img')[0].get('src', 'No disponible'),
            "nombre": player.find('td', class_='hauptlink').get_text(strip=True),
            "dorsal": player.find('div', class_='rn_nummer').get_text(strip=True),
            "position": player.select('.inline-table tr:last-of-type td')[0].get_text(strip=True),
            "fecha_nacimiento": player.select('tr td:nth-child(3)')[0].get_text(strip=True)[:10],
            "edad": player.select('tr td:nth-child(3)')[0].get_text(strip=True)[12:-1],
            "pais": player.select('tr td:nth-child(4) img')[0].get('alt', 'Desconocido'),
            "altura": player.select('tr td:nth-child(5)')[0].get_text(strip=True),
            "pie": player.select('tr td:nth-child(6)')[0].get_text(strip=True),
            "fecha_fichaje": player.select('tr td:nth-child(7)')[0].get_text(strip=True),
            "equipo_anterior": player.select('tr td:nth-child(8) img')[0].get('alt', 'Desconocido') if player.select('tr td:nth-child(8) img') else 'Desconocido',
            "fecha_final_contrato": player.select('tr td:nth-child(9)')[0].get_text(strip=True),
            "valor_de_mercado": player.select('tr td:nth-child(10)')[0].get_text(strip=True)[:-7]
        }
        
        jugadores.append(jugador)

    return jugadores

