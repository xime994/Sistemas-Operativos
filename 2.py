print("Vector2: media de temperaturas.")

Suma = 0
Media = 0.0
C = 0
Temp = [] 

print("Ingrese cantidad de Temperaturas: ")
N = int( input())

for i in range(N):
    temperatura = float( input("Ingrese Temperatura {0}: ".format(i + 1) ))
    Temp.append(temperatura)
    Suma = Suma + Temp[i]
Media = Suma / N 

for tempElement in Temp: 
    if tempElement >= Media:
        C = C + 1
        print(tempElement)
print("\nsalida: ")
print ("La media es ", Media)
print ("Total de temperaturas >= a la media es", C)