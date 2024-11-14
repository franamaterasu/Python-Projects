from modules.menu import menu

class ProgramaCalculadora:
  def __init__(self):
    pass
  
  def iniciar(self):
    print('Bienvenido a la calculadora. ¿Que operación quieres hacer?')
    menu()
  
  
if __name__ == "__main__":
  app = ProgramaCalculadora()
  app.iniciar()
