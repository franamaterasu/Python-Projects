from menu import menu

class ProgramaBancario:
  def __init__(self):
    self.cuenta = None
    
  def iniciar(self):
    print('Bienvenido al programa bancario, ¿que acción quieres realizar?:')
    menu()

if __name__ == '__main__':
  app = ProgramaBancario()
  app.iniciar()
