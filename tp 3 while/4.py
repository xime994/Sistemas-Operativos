import random
secreto = random.randint(1, 10)

for intento in range(3):
    adivina = int(input("Adiviná el número (1 al 10): "))
    if adivina == secreto:
        print("¡Correcto!")
        break
    else:
        print("Incorrecto")
else:
    print(f"Perdiste. El número era {secreto}")