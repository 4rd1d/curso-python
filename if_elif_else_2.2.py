print("COMPARADOR DE NUMEROS")
n1 = float(input("Escriba un numero: "))
n2 = float(input(("Escriba otro numero: ")))

if n1 == n2:
    print("Los 2 numeros son iguales")
else:
    if n1 > n2:
        print(f"Menor: {n2}; Mayor: {n1}")
    else:
        print(f"Menor: {n1}; Mayor: {n2}")
