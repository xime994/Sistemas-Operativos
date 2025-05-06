while True:
    capital = float(input("¿Cuánto dinero tienes? "))
    interes = float(input("¿Cuál es el interés? (de 1 a 99) "))
    años = int(input("¿Cuántos años estará el dinero? "))

 
    if capital >= 0 and 0 < interes < 100 and años > 0:
        break
    else:
        print("Los datos no son válidos, inténtalo otra vez.")

for i in range(años):
    capital = capital * (1 + interes / 100)

print(f"Después de {años} años tendrás {capital:.2f} soles.")