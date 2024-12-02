#1. Realizar un programa que calcule la media de los 100 primeros números pares.Y la cantidad de impares
suma= 0
contp = 0
contimp = 0
med=0


for num in range(1, 101):
    if num % 2 == 0:
        suma+= num  
        contp += 1  
    else:
        contimp += 1  


med = suma / contimp 


print(f"La media de los primeros 100 numeros pares es: {med}")
print(f"El numero de impares entre 1 y 100 es: {contimp}")