import csv

def guardar_jugadores_csv(jugadores, filename='./data/players.csv'):
    # Guarda la lista de jugadores en un archivo CSV
    if jugadores:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=jugadores[0].keys())
            writer.writeheader()
            for jugador in jugadores:
                writer.writerow(jugador)
        print(f"Datos de los jugadores guardados en '{filename}'")
    else:
        print("No se encontraron jugadores para guardar.")
