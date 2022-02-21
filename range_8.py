print("LISTA DE UN VALOR A OTRO")
n1 = int(input("Escriba el numero entero inicial: "))
n2 = int(input("Escriba el numero entero final: "))
if n1 < n2:
    print(list(range(n1,n2+1)))
elif n1 > n2:
    print(list(range(n1,n2-1,-1)))
else:
    print(list(range(n1,n2+1)))