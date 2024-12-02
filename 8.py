#8.Tabla de multiplicar con métodos
def tabla(num):
    print(f"\nTabla de multiplicar {num} ")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

num = int(input("Introduce un número para utilizar la tabla de multiplicar: "))
tabla(num)