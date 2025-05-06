x = int(input("Ingrese el valor de x: "))
e = 1
num = 1
den = 1
t = 1

while t >= 0.00001:
    num = num * x
    den = den * (e)
    t = num / den
    e = e + t

print("El resultado es:", e)