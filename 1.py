
print("Vector1: lectura de n elementos enteros.")

i = 1
F = []

print("Ingrese Número de elementos a Ingresar: ")
numElementos = int( input())

while i <= numElementos:
    elemento = int( input("Ingrese Elemento: "))
    F.append(elemento)
    i = i + 1

print("\nsalida: ")

print(F)