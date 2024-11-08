import random

def jugar():
  numero_secreto = random.randint(1, 10)
  intentos = 0
  
  while intentos < 3:
    numero_seleccionado = int(input('Inserta tu número: '))
  
    if numero_seleccionado != numero_secreto:
      intentos += 1
      if intentos < 3:
        print('El número no es correcto, intentalo de nuevo')
        print(f"Número de intentos: {intentos}")
      else:
        print(f"Lo sentimos, has superado el número de intentos posibles.\nEl número secreto era {numero_secreto}")
    else:
      print(f'Felicidades, has acertado, el número secreto es {numero_secreto}')
      break
    
def main():
  jugar()
  
  
if __name__ == "__main__":
  main()
