a1 = 1
a2 = 1
an = 1
rango = 2

while an <= 300:
    an = a1 + (2 * a2)
    a1 = a2
    a2 = an
    rango += 1

print("El rango es:", rango)
print("El resultado es:", an)