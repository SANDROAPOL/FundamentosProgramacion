# 10. Calificación final
promedio_parciales = float(input("Ingrese el promedio de sus tres parciales: "))
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print("Calificación final:", calificacion_final)
