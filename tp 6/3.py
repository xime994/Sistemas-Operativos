contador = 0 

for num in range(1, 1001):
    if num < 2:
        continue  

    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f"{num} es primo")
        contador += 1

print(f"Entre 1 y 1000 hay {contador} números primos.")