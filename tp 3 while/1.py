total = 0
for i in range(5):
    nota = float(input(f"Ingresá la nota del alumno {i+1}: "))
    total += nota

promedio = total / 5
print(f"El promedio es: {promedio}")

if promedio > 7:
    print("¡Buen promedio!")