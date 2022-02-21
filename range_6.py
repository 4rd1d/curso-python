print("LISTAS DESDE CERO HASTA VALOR")
n = int(input("Escriba un numero entero: "))
if n >= 0:
    print(list(range(0,n+1)))
elif n <= 0:
    print(list(range(0,n-1,-1)))