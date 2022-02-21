print("MULTIPLO ENTRE VALORES")
n1 = int(input("Escriba el numero entero inicial: "))
n2 = int(input("Escriba el numero entero final: "))
if n1 > n2:
    print("¡El numero final debe ser mayor que el inicial!")
else:
    n3 = int(input("De que numero quiere los multiplos?: "))
    if n3 <= 0:
        print("¡Los multiplos deben ser de un numero entero mayor a cero!")
    elif n1 % n3 == 0 and n3 < n2:
        print(f"Entre {n1} y {n2} hay {len(range(n1,n2+1,n3))} multiplos de {n3}:")
        print(list(range(n1, n2 + 1, n3)))
    elif n1 % n3 != 0 and n3 < n2:
        print(f"Entre {n1} y {n2} hay {len(range(n1+1,n2,n3))} multiplos de {n3}:")
        print(list(range(n1+1,n2,n3)))
    elif n3 > n2:
        print(f"Entre {n1} y {n2} hay {len(range(n1%n3==0))} multiplos de {n3}:")
        print(list(range(n1%n3==0)))
