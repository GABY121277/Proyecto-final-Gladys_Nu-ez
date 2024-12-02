#2. Realizar un programa que lea 5 calificaciones y calcule el promedio del alumno y si promedio mayor o igual que 70 aprobó, en caso contrario reprobó
suma = 0

print("Ingrese 5 calificaciones:")
for _ in range(5):
    calif = float(input("Calificación: "))
    suma += calif

promedio = suma / 5

if promedio >= 70:
    print(f"Felicidades, ha acreditado con la calificación de: {promedio}")
else:
    print(f"Lo sentimos, no ha acreditado. Su calificación es de: {promedio}")