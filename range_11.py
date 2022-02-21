print("PARES ENTRE VALORES")
n1 = int(input("Escriba el numero entero inicial: "))
n2 = int(input("Escriba el numero entero final: "))
if n1 % 2 == 0 and n1 < n2:
    print(list(range(n1,n2+1,2)))
elif n1 % 2 != 0 and n1 < n2:
    print(list(range(n1+1,n2+2,2)))
elif n1 == n2:
    print(list(range(n1,n2+1)))
else:
    print("¡El numero final debe ser mayor que el inicial")