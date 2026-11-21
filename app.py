tareas = []


def mostrar_menu():
    print("\n==============================")
    print("      GESTOR DE TAREAS")
    print("==============================")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("==============================")


def agregar_tarea():
    titulo = input("Ingrese el nombre de la tarea: ")
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada correctamente.")


def listar_tareas():
    print("\n===== LISTA DE TAREAS =====")

    if not tareas:
        print("No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea['titulo']}")


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no disponible todavía.")
