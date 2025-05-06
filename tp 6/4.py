n = int(input("Ingrese un número: "))

while n > 0:
    digito = n % 10
    print(digito)
    n = n // 10