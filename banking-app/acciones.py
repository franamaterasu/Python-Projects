"""
acciones.py

Este módulo proporciona funciones para gestionar una cuenta bancaria simple. 

Funciones:
- ingresar(cantidad): Aumenta el saldo de la cuenta en la cantidad especificada, si la cantidad es positiva.
- sacar(cantidad): Disminuye el saldo de la cuenta en la cantidad especificada si la cantidad es positiva. Solicita confirmación si la cantidad es mayor que el saldo actual.
- mostrar_cuenta(): Muestra el saldo actual de la cuenta.
"""

cantidad_total = 0


def ingresar(cantidad):
    """
    Aumenta el saldo de la cuenta en la cantidad especificada.

    Args:
        cantidad (float): La cantidad de dinero a ingresar. Debe ser mayor que 0.

    Returns:
        None
    """

    global cantidad_total
    if cantidad > 0:
        cantidad_total += cantidad
        print(f"La cantidad de {cantidad}€ ha sido ingresada")
    else:
        print("La cantidad debe ser mayor que 0")


def sacar(cantidad):
    """
    Disminuye el saldo de la cuenta en la cantidad especificada, si es posible.

    Si la cantidad a sacar es mayor que el saldo actual, solicita confirmación al usuario.

    Args:
        cantidad (float): La cantidad de dinero a sacar. Debe ser mayor que 0.

    Returns:
        None
    """

    global cantidad_total

    if cantidad <= 0:
        print("La cantidad debe ser mayor que 0")
        return

    if cantidad > cantidad_total:
        confirmacion = (
            input("¿Quieres sacar más cantidad de la que dispones? (s/n): ")
            .strip()
            .lower()
        )

        if confirmacion == "s":
            cantidad_total -= cantidad
            print(f"La cantidad de {cantidad}€ ha sido sacada")
        elif confirmacion == "n":
            print("Operación cancelada")
        else:
            print("Confirmación no válida. Operación cancelada")
    else:
        cantidad_total -= cantidad
        print(f"La cantidad de {cantidad}€ ha sido sacada")


def mostrar_cuenta():
    """
    Muestra el saldo actual de la cuenta.

    Args:
        None

    Returns:
        None
    """

    print(f"La cantidad de ingresos en tu cuenta es de: {cantidad_total}€")
