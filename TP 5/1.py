horas = int(input("Horas trabajadas: "))
valor_hora = float(input("Valor por hora: "))

if horas > 40:
    extra = horas - 40
    sueldo = (40 * valor_hora) + (extra * valor_hora * 2)
else:
    sueldo = horas * valor_hora

print(f"Sueldo total: ${sueldo:.2f}")