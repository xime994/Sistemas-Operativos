positivos = negativos = 0
suma_pos = suma_neg = 0

for i in range(10):
    num = int(input(f"Ingresá el número {i+1}: "))
    if num > 0:
        positivos += 1
        suma_pos += num
    elif num < 0:
        negativos += 1
        suma_neg += num

if positivos > 0:
    print(f"Promedio positivos: {suma_pos / positivos}")
else:
    print("No hubo números positivos.")

if negativos > 0:
    print(f"Promedio negativos: {suma_neg / negativos}")
else:
    print("No hubo números negativos.")