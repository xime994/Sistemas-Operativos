calificacion = float(input("Ingrese la calificación del alumno: "))

if calificacion > 10:
  print("Calificación inválida. Debe ser menor o igual a 10.")
elif calificacion >= 7:
  print("Aprobado")
else:
  print("Reprobado")