from random import randint
print("PARES Y NONES")
numero_dados = int(input("Numero de dados: "))
if numero_dados < 1:
    print("IMPOSIBLE")
else:
    print("Dados: ", end=" ")
    cuenta1 = 0
    cuenta2 = 0
    for i in range(numero_dados):
        dados = randint(1, 6)
        print(dados, end=" ")
        if dados % 2 == 0:  # pares
            cuenta1 = cuenta1 + 1
        elif dados % 2 != 0:  # impares
            cuenta2 = cuenta2 + 1
    print()
    if cuenta1 > cuenta2:
        print("Ha ganado el jugador de los pares")
    elif cuenta1 < cuenta2:
        print("Ha gando el jugador impar")
    else:
        print("Han empatado")
