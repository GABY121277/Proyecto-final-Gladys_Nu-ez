#9. Métodos.Leer tres numeros y sumar, multiplicar, raiz y potencia
import math

def suma(num1, num2, num3):
    return num1 + num2 + num3

def mult(num1, num2, num3):
    return num1 * num2 * num3

def raiz(num):
    return math.sqrt(num)

def pot(num):
    return math.pow(num, 2)

print("MENÚ:\n1. SUMAR\n2. MULTIPLICAR\n3. RAÍZ CUADRADA\n4.POTENCIA")

x = int(input("Elige una opción: "))

if x == 1:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    print("Resultado de la suma:", suma(num1, num2, num3))

elif x == 2:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    print("Resultado de la multiplicación:", mult(num1, num2, num3))

elif x == 3:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    print(f"Raíz cuadrada de {num1}: {raiz(num1)}")
    print(f"Raíz cuadrada de {num2}: {raiz(num2)}")
    print(f"Raíz cuadrada de {num3}: {raiz(num3)}")

elif x == 4:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    print(f"{num1} al cuadrado: {pot(num1)}")
    print(f"{num2} al cuadrado: {pot(num2)}")
    print(f"{num3} al cuadrado: {pot(num3)}")

else:
    print("Opción no válida.")