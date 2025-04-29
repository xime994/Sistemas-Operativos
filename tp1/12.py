sueldo = float(input("Ingrese el sueldo del trabajador: "))

if sueldo < 1000:
  aumento = sueldo * 0.15
  sueldo_final = sueldo + aumento
  print(f"El sueldo con el aumento del 15% es: ${sueldo_final:.2f}")
else:
  print(f"El sueldo es de: ${sueldo:.2f}. No aplica aumento.")