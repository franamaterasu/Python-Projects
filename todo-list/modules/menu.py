from .creador_de_tareas import CreadorDeTareas


def menu():
    """
    Muestra un menú interactivo para gestionar la lista de tareas.

    El menú ofrece la siguientes opciones:
      1. Agregar tarea: Permite al usuario agregar una nueva tarea
      2. Mostrar tareas: Permite al usuario ver todas las tareas
      3. Eliminar tarea: Permite al usuario eliminar una tarea por su índice
      4. Salir del programa: Permite al usuario terminar la ejecucación de programa

    El bucle se ejecuta continuamente hasta que el usuario elige la opción 'Salir del programa'
    """
    
    creador_tareas = CreadorDeTareas()
    
    while True:
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Salir del programa")
        
        

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                tarea = input("Inserta una tarea: ")
                creador_tareas.agregar_tarea(tarea)
                print(f"La tarea '{tarea}' ha sido agregada")
            except ValueError:
                print("Por favor inserta una tarea valida")
            creador_tareas.mostrar_tareas()
        elif opcion == "2":
            creador_tareas.mostrar_tareas()
        elif opcion == "3":
            try:
                indice = int(input("Introduce el índice de la tarea a eliminar: ")) - 1
                creador_tareas.eliminar_tarea(indice)
                print(f"La tarea con índice {indice + 1} ha sido eliminada")
                creador_tareas.mostrar_tareas()
            except ValueError:
                print("Por favor, inserta un índice válido.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida")
