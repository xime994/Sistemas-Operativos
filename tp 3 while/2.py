ninios = adolescentes = adultos = 0

while True:
    edad = int(input("Ingresá una edad (0 para salir): "))
    if edad == 0:
        break
    if edad < 13:
        ninios += 1
    elif edad <= 17:
        adolescentes += 1
    else:
        adultos += 1

print("Niños:", ninios)
print("Adolescentes:", adolescentes)
print("Adultos:", adultos)