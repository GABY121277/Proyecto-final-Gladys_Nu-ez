#6.Calcular la media de 20 números
suma = 0


print("Introduce 20 números:")
for i in range(20):
    numero = float(input(" "))
    suma += numero


media = suma / 20


print(f"\nLa media de los 20 números es: {media}")