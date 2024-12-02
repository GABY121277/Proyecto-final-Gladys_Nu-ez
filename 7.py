#7.Números primos del 1 al 1000
contador = 0
print("Números primos:")
for num in range(1, 1001):
    div = 0
    for i in range(1, num + 1):
        if num % i == 0:
            div += 1
            
    if div == 2:
        print(num)
        contador += 1  
        
print(f"Total números primos: {contador}")