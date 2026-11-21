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
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['titulo']} - {estado}")


def completar_tarea():
    if not tareas:
        print("No hay tareas para completar.")
        return

    listar_tareas()
    try:
        numero = int(input("Ingrese el numero de tarea: "))

        if 1 <= numero <= len(tareas):
            tareas[numero - 1]["completada"] = True
            print("Tarea completada correctamente.")
        else:
            print("Numero de tarea no valido.")
    except ValueError:
        print("Ingrese un numero valido.")


def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar.")
        return

    listar_tareas()
    try:
        numero = int(input("Ingrese el numero de tarea: "))

        if 1 <= numero <= len(tareas):
            tarea = tareas.pop(numero - 1)
            print(f"Tarea '{tarea['titulo']}' eliminada.")
        else:
            print("Numero de tarea no valido.")
    except ValueError:
        print("Ingrese un numero valido.")


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida.")
