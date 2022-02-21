from random import randint
print("EL DADO MAS ALTO (2)")
cantidad_dados = int(input("Numero de dados: "))
if cantidad_dados < 0:
    print("IMPOSIBLE")
else:
    dado_mas_alto_1 = 1
    print(f"Jugador 1: ", end=" ")
    for i in range(cantidad_dados):
        numero_dado = randint(1, 6)
        print(numero_dado, end=" ")
        if numero_dado > dado_mas_alto_1:
            dado_mas_alto_1 = numero_dado

    print()
    dado_mas_alto_2 = 1
    print("Jugador 2: ", end=" ")
    for i in range(cantidad_dados):
        numero_dado_2 = randint(1, 6)
        print(numero_dado_2, end=" ")
        if numero_dado_2 > dado_mas_alto_2:
            dado_mas_alto_2 = numero_dado_2

    print()
    if dado_mas_alto_1 > dado_mas_alto_2:
        print(f"Ha ganado el jugador 1")
    elif dado_mas_alto_1 < dado_mas_alto_2:
        print(f"Ha ganado el jugador 2")
    else:
        print("Han empatado")
