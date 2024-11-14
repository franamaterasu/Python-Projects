class CuentaBancaria:
  def __init__(self, saldo_inicial = 0):
    self.saldo = saldo_inicial

  def ingresar(self, cantidad):
    """
      Aumentar el saldo de la cuenta con la cantidad que se le indica
      
      Args:
        cantidad (float): Cantidad de dinero para ingresar. (Debe ser mayor que 0)
    """
    
    if cantidad > 0:
      self.saldo += cantidad
      
      print(f'La cantidad de {cantidad}€ ha sido ingresada')
    
    else:
      print('La cantidad debe ser mayor que 0')
      
  
  def sacar(self, cantidad):
    """
      Disminuir el saldo de la cuenta con la cantidad ingresada.
      
      Dicha cantidad debe ser menor al saldo total de la cuenta
      
      Args:
        cantidad (float): Cantidad de dinero para sacar (Debe ser mayor que 0)
    """
    
    if cantidad <= 0:
      print('La cantidad debe ser mayor que 0')
      
    if cantidad > self.saldo:
      print(f"No puedes sacar más del dinero que dispone en la cuenta ({self.saldo}€)")
    else:
      self.saldo -= cantidad
      print(f"Has sacado de la cuenta la cantidad de {cantidad}€, actualmente tu saldo es de {self.saldo}€")
  
  
  def mostrar_cuenta(self):
    """
    Mostrar el saldo actual de la cuenta
    """
    
    print(f'El saldo actual de tu cuanto es {self.saldo}€')
    
