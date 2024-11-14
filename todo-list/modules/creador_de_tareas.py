class CreadorDeTareas:
  def __init__(self):
    self.lista_tareas = []
    
  def agregar_tarea(self, tarea):
    """
      Agrega una nueva tarea a la lista de tareas.

      Args:
          tarea (str): La tarea a agregar a la lista.
    """
    self.lista_tareas.append(tarea)
    
  def eliminar_tarea(self, index):
    """
    Elimina una tarea de la lista de tareas por su índice.

    Args:
        index (int): El índice de la tarea a eliminar (basado en 0).

    Raises:
        IndexError: Si el índice está fuera de los límites de la lista.
    """
    if 0 <= index < len(self.lista_tareas):
      self.lista_tareas.pop(index)
    else:
      print(f"No existe la tarea con el índice {index}")
      
  def mostrar_tareas(self):
    """
    Muestra todas las tareas en la lista con su índice correspondiente.

    Si la lista está vacía, imprime un mensaje indicando que no hay tareas.
    """
    if not self.lista_tareas:
      print('La lista de tareas está vacia')
    else:
      for i, tarea in enumerate(self.lista_tareas):
        print(f'{i + 1}. {tarea}')
