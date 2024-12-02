#5. Tabla de multiplicar, dado un número en for y en while
x = int(input("MENÚ:\n1. FOR\n2. WHILE: "))
num= int(input("Introduce un número para utilizar la tabla de multiplicar: "))

if x == 1:
    print(f"\nTabla de multiplicar de {num} usando FOR:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

elif x == 2:
    print(f"\nTabla de multiplicar de {num} usando WHILE:")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

else:
    print("Opción no válida.")