print("LISTAS ENTRE DOS NUMEROS")
n1 = int(input("Escriba un numero entero: "))
n2 = int(input(f"Escriba otro numero entero mayor que {n1}: "))
if n1 < n2:
    print(list(range(n1,n2+1)))
    print(list(range(n2-1,n1-1,-1)))
    print(list(range(n1+1,n2+2)))
    print((list(range(n2-1,n1,-1))))
    print(list(range(n1,n2+1)) + list(range(n2-1,n1-1,-1)))
elif n1 > n2:
    print(f"Le he pedido un numero mayor que {n1}")