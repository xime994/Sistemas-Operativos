hay_par = False

for i in range(5):
    num = int(input(f"Ingresá el número {i+1}: "))
    if num % 2 == 0:
        hay_par = True

if hay_par:
    print("Hay al menos un número par.")
else:
    print("No hay números pares.")