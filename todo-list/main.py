from modules.menu import menu


class ProgramaTareas:
  def __init__(self):
    pass
  
  def iniciar(self):
    print('Bienvenido al creador de tareas. ¿Que operación quieres hacer')
    menu()

if __name__ == "__main__":
  app = ProgramaTareas()
  app.iniciar()
  
