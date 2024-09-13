from weather import get_weather_data, parse_weather_data


def main():
    """
    Función principal que gestiona la interacción con el usuario y coordina las otras funciones.

    Permite al usuario insertar una ciudad y mostrar los datos climáticos de dicha ciudad
    """

    while True:

        city = input("Inserta una ciudad: ")

        if city.lower() == "exit":
            break

        if not city.strip():
            print("Por favor, inserta una ciudad válida")
            continue

        data = get_weather_data(city)

        if data:
            weather_data = parse_weather_data(data)
            print(weather_data)


if __name__ == "__main__":
    main()
