# Clase Tarea que representa una tarea
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def mostrar_info(self):
        estado = "Completada" if self.completada else "Pendiente"
        print(f"Tarea: {self.descripcion} - Estado: {estado}")

# Clase ListaDeTareas que maneja las tareas
class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if not self.tareas:
            print("No tienes tareas pendientes.")
        else:
            for tarea in self.tareas:
                tarea.mostrar_info()

    def marcar_tarea_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea.descripcion.lower() == descripcion.lower():
                tarea.marcar_completada()
                print(f"La tarea '{tarea.descripcion}' ha sido marcada como completada.")
                return
        print(f"No se encontró la tarea: {descripcion}")

# Función principal para manejar el flujo del programa
def main():
    lista_tareas = ListaDeTareas()

    while True:
        print("\nOpciones:")
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            tarea = Tarea(descripcion)
            lista_tareas.agregar_tarea(tarea)
            print(f"Tarea '{descripcion}' agregada.")

        elif opcion == "2":
            descripcion = input("Ingrese la descripción de la tarea que completaste: ")
            lista_tareas.marcar_tarea_completada(descripcion)

        elif opcion == "3":
            lista_tareas.mostrar_tareas()

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()

#