correcta = "python123"
intentos = 0

while intentos < 3:
    clave = input("Ingresá la contraseña: ")
    if clave == correcta:
        print("¡Acceso concedido!")
        break
    else:
        print("Contraseña incorrecta.")
        intentos += 1

if intentos == 3:
    print("Acceso bloqueado")