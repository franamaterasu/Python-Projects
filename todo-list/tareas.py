tareas = []


def agregar_tarea(tarea):
    """
    Agrega una nueva tarea a la lista de tareas.

    Args:
      tarea (str): La tarea que se va agregar
    """
    tareas.append(tarea)


def eliminar_tarea(index):
    """
    Elimina una tarea de la lista de tareas por su índice.

    Args:
      index (int): El índice de la tarea a eliminar (basada en 0)
    """
    if 0 <= index < len(tareas):
        tareas.pop(index)
    else:
        print(f"No existe la tarea con el índice {index}")


def mostrar_tareas():
    """
    Muestra todas las tareas de la lista de tareas con su índice correspondiente.

    Si no hay tareas, devuelve un mensaje indicando que la lista está vacia.
    """
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea}")
