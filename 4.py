#4. Conversión de los números romanos 1000-3000
numero = int(input("Ingresa un número entre 1000 y 3000: "))

if 1000 <= numero <= 3000:
    romano = ""
    
    if numero >= 1000:
        miles = numero // 1000
        numero %= 1000
        if miles == 3:
            romano += "MMM"
        elif miles == 2:
            romano += "MM"
        elif miles == 1:
            romano += "M"

    if numero >= 100:
        centenas = numero // 100
        numero %= 100
        if centenas == 9:
            romano += "CM"
        elif centenas == 8:
            romano += "DCCC"
        elif centenas == 7:
            romano += "DCC"
        elif centenas == 6:
            romano += "DC"
        elif centenas == 5:
            romano += "D"
        elif centenas == 4:
            romano += "CD"
        elif centenas == 3:
            romano += "CCC"
        elif centenas == 2:
            romano += "CC"
        elif centenas == 1:
            romano += "C"

    if numero >= 10:
        decenas = numero // 10
        numero %= 10
        if decenas == 9:
            romano += "XC"
        elif decenas == 8:
            romano += "LXXX"
        elif decenas == 7:
            romano += "LXX"
        elif decenas == 6:
            romano += "LX"
        elif decenas == 5:
            romano += "L"
        elif decenas == 4:
            romano += "XL"
        elif decenas == 3:
            romano += "XXX"
        elif decenas == 2:
            romano += "XX"
        elif decenas == 1:
            romano += "X"

    if numero > 0:
        if numero == 9:
            romano += "IX"
        elif numero == 8:
            romano += "VIII"
        elif numero == 7:
            romano += "VII"
        elif numero == 6:
            romano += "VI"
        elif numero == 5:
            romano += "V"
        elif numero == 4:
            romano += "IV"
        elif numero == 3:
            romano += "III"
        elif numero == 2:
            romano += "II"
        elif numero == 1:
            romano += "I"
    
    print("Número romano:", romano)
else:
    print("El número está fuera del rango.")