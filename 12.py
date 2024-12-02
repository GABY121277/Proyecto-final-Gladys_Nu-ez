#12.Ingresar 10 números de forma desordenada,ordenar ascendente y descendente
num = [1, 5, 9, 33, 7, 8, 10, 6, 12, 4]


num.sort()  
print("Números ascendentes:")
for nums in num:
    print(nums)


num.sort(reverse=True) 
print("\nNúmeros descendentes:")
for nums in num:
    print(nums)