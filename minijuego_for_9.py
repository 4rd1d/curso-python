from random import randint
print("DADO MAS ALTO Y MAS BAJO")
dados = int(input("Numero de dados: "))
if dados < 1:
    print("IMPOSIBLE")
else:
    valor_mayor_1 = 0
    valor_menor_1 = 6
    valor_mayor_2 = 0
    valor_menor_2 = 6
    print(f"Jugador 1: ", end=" ")  # PRIMER JUGADOR
    for i in range(dados):
        valor_dado_1 = randint(1, 6)
        print(valor_dado_1, end=" ")
        if valor_dado_1 > valor_mayor_1:
            valor_mayor_1 = valor_dado_1
        elif valor_menor_1 > valor_dado_1:
            valor_menor_1 = valor_dado_1

    print()
    print(f"Jugador 2: ", end=" ")  # SEGUNDO JUGADOR
    for i in range(dados):
        valor_dado_2 = randint(1, 6)
        print(valor_dado_2, end=" ")
        if valor_dado_2 > valor_mayor_2:
            valor_mayor_2 = valor_dado_2
        elif valor_menor_2 > valor_dado_2:
            valor_menor_2 = valor_dado_2
    print()

    if valor_mayor_1 + valor_menor_1 > valor_mayor_2 + valor_menor_2:
        print(f"Ha ganado el jugador 1")
    elif valor_mayor_1 + valor_menor_1 < valor_mayor_2 + valor_menor_2:
        print(f"Ha ganado el jugador 2")
    else:
        print("Han empatado")

    print(valor_mayor_1, valor_menor_1, valor_mayor_2, valor_menor_2)

