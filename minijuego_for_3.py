from random import randint
jugador = int(input("Numero de jugadores: "))
if jugador < 1:
    print("¡Imposible!")
else:
    valor = int(input("Valor a conseguir: "))
    if valor > 6:
        print(f"¡Imposible conseguir un {valor}!")
    else:
        for i in range(1, jugador+1):
            a = randint(1, 6)
            if a == valor:
                print(f"Jugador {i}: {a} CONSEGUIDO")
            elif randint(1, 6) != valor:
                print(f"Jugador {i}: {a}")
