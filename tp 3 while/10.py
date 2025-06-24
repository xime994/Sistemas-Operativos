while True:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Decir adiós")
    print("3. Salir")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print("¡Hola! ")
    elif opcion == "2":
        print("¡Adiós! ")
    elif opcion == "3":
        print("Saliendo del menú...")
        break
    else:
        print("Opción inválida.")