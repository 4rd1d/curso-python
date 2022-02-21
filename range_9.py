print("LISTA DE MENOR A MAYOR")
n1 = int(input("Escriba un numero entero: "))
n2 = int(input("Escriba otro numero entero: "))
if n1 < n2:
    print(list(range(n1+1,n2)))
elif n1 > n2:
    print(list(range(n2+1,n1)))
else:
    print(list(range(n1,n2)))
