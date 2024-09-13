"""
menu.py

Este módulo proporciona una interfaz de menú interactiva para gestionar una cuenta bancaria simple.
Permite al usuario ingresar dinero, sacar dinero, mostrar el saldo de la cuenta y salir del programa.

Funciones:
- menu(): Muestra el menú interactivo y gestiona las opciones del usuario.
"""

from acciones import ingresar, sacar, mostrar_cuenta


def menu():
    """
    Muestra un menú interactivo para gestionar la cuenta bancaria.

    El menú ofrece las siguientes opciones:
      1. Ingresar dinero: Permite al usuario ingresar una cantidad de dinero a la cuenta.
      2. Sacar dinero: Permite al usuario retirar una cantidad de dinero de la cuenta.
      3. Mostrar la cuenta: Muestra el saldo actual de la cuenta.
      4. Salir de la cuenta: Termina la ejecución del programa.

    El bucle se ejecuta continuamente hasta que el usuario elige la opción 'Salir de la cuenta'.

    Args:
        None

    Returns:
        None
    """

    while True:
        print("1. Ingresar dinero")
        print("2. Sacar dinero")
        print("3. Mostrar la cuenta")
        print("4. Salir de la cuenta")

        option = input("Selecciona una opcion: ")

        if option == "1":
            try:
                cantidad = int(input("Inserta la cantidad que quieres ingresar: "))
                ingresar(cantidad)

            except ValueError:
                print("Por favor, inserta una cantidad válida")
        elif option == "2":
            try:
                cantidad = int(input("Inserta la cantidad que quieres sacar: "))
                sacar(cantidad)
            except ValueError:
                print("Por favor, inserta una cantidad válida")
        elif option == "3":
            mostrar_cuenta()
        elif option == "4":
            print("Saliendo de la cuenta...")
            break
        else:
            print("Opción no valida. Por favor, selecciona una opción del 1 al 4")
