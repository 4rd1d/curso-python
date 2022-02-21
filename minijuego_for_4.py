from random import randint
print("OBTENER VALOR")
numero = int(input("Numero de dados: "))
if numero <= 0:
    print("¡Imposible!")
else:
    valor = int(input("Valor a conseguir: "))
    print("Dados: ", end=" ")
    encontrado = False
    for i in range(numero):
        a = randint(1, 6)
        print(a, end=" ")
        if valor == a:
            encontrado = True
    if encontrado:
        print("\nEl jugador ha ganado")
    else:
        print("\nEl jugador ha perdido")
