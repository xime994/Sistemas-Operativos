menores_0 = mayores_30 = 0

while True:
    temp = float(input("Ingresá una temperatura (-100 para salir): "))
    if temp == -100:
        break
    if temp < 0:
        menores_0 += 1
    if temp >= 30:
        mayores_30 += 1

print("Temperaturas < 0°C:", menores_0)
print("Temperaturas >= 30°C:", mayores_30)