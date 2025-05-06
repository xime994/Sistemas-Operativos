while True:
    numero = int(input("Escribe un número (negativo para salir): "))
    
    if numero < 0:
        break 

    suma = 0  
    for i in range(1, numero + 1):
        if numero % i == 0:
            suma += i  

    print(f"La suma de los divisores de {numero} es: {suma}")