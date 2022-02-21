print("LISTAS A PARTIR DE VALOR")
n = int(input("Escriba un numero entero mayor que 0: "))
if n <= 0:
    print("Le he pedido un numero entero mayor que 0")
else:
    print(list(range(0,n+1)))
    print(list(range(n,-1,-1)))
    print(list(range(1,n)))
    print(list(range(n-1,0,-1)))
    print(list(range(n+1)) + list(range(n-1,-1,-1)))