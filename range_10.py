print("VALORES CONSECUTIVOS")
n = int(input("Escriba el numero entero inicial: "))
m = int(input("Escriba cuantos valores quiere: "))
if m >= 0:# m < 0
    print(list(range(n,n+m)))
else:
    print("¡La cantidad de valores no puede ser negativa")
