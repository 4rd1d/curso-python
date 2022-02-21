print("COMPARAR DE TRES NUMEROS")
n1 = int(input("Escriba un numero: "))
n2 = int(input("Escriba otro numero: "))
n3 = int(input("Escriba otro numero mas: "))

if n1 != n2 and n3 != n2 and n3 != n1:
    print("Los tres numeros que ha escrito son distintos")
elif n1 == n2 and n3 == n2 and n3 == n1:
    print("Ha escrito tres veces el mismo numero")
else:
    print("Ha escrito uno de los numeros dos veces")