from .calculadora import Calculadora

def menu():
  while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    option = input("Selecciona una opción: ")

    if option == "5":
        print("Saliendo de la calculadora...")
        break
    elif option in ["1", "2", "3", "4"]:
        num1 = float(input('Elige el primer número: '))
        num2 = float(input('Elige el segundo número: '))

        machine = Calculadora(num1, num2)

        if option == "1":
            print(f'La suma es: {machine.sumar()}')
        elif option == "2":
            print(f'La resta es: {machine.restar()}')
        elif option == "3":
            print(f'La multiplicación es: {machine.multiplicar()}')
        elif option == "4":
            print(f'La división es: {machine.dividir()}')
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 5")
