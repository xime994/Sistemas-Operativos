print("Vector3: ordenar y quitar elementos repetidos del vector.")

VEC = [] 
print("Ingrese número de elementos del vector")
N = int( input())

if 1 <= N and N <= 200:
    for i in range(1,N+1):
        elemento = int( input("Ingrese Entero {0}: ".format(i)))
    VEC.append(elemento)
    i = 0
    #TODO:
    lista_nueva = [] 
    for elemento in VEC:

        if elemento not in lista_nueva:
            lista_nueva.append(elemento)

lista_nueva.sort()

print("\nsalida: ")
print(lista_nueva)