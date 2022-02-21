print("COMPARADOR DE MULTIPLOS")
n1 = int(input("Escriba un numero: "))
n2 = int(input("Escriba otro numero: "))

if n1 <= 0 or n2 <= 0:
    if n1 < 0 or n2 < 0:
        print("Lo siento, este programa no admite valores negativos")
    else:
        print("Lo siento, este programa no admite valores nulos")
elif n1 > n2:
    if n1 % n2 == 0:
        print(f"{n1} es multiplo de {n2}")
    else:
        print(f"{n1} no es multiplo de {n2}")
elif n1 < n2:
    if n2 % n1 == 0:
        print(f"{n2} es multiplo de {n1}")
    else:
        print(f"{n2} no es multiplo de {n1}")
else:
    print(f"{n1} es multiplo de {n2}")