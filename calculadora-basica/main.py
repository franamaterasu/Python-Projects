
# importamos las funciones del módulo 'operaciones' y del módulo 'menu'
from modules.operaciones import suma, resta, multiplicacion, division
from modules.menu import mostrar_menu

# creamos la función 'main' que contiene el código principal
def main():
  while True:
    mostrar_menu()
    
    opcion = int(input('Selecciona una opción: ' ))
    
    if opcion in [1, 2, 3, 4]:
      num1 = float(input('Elige el primer número: '))
      num2 = float(input('Elige el segundo número: '))
    
      if opcion == 1:
        print(suma(num1, num2))
      elif opcion == 2:
        print(resta(num1, num2))
      elif opcion == 3:
        print(multiplicacion(num1, num2))
      elif opcion == 4:
        print(division(num1,num2))
    if opcion == 5:
        break
    if opcion not in [1, 2, 3, 4, 5]:
      print('Elija una opción válida')
      continue

# Ejecutamos el programa principal
if __name__ == '__main__':
  main()
