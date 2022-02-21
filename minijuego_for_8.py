from random import randint
jugadores = int(input("Numero de jugadores: "))
if jugadores < 1:
    print("IMPOSIBLE")
else:
    dado_mas_alto = 6
    jugador = 0
    for i in range(1, jugadores+1):
        numero_del_dado = randint(1, 6)
        print(f"Jugador {i}: {numero_del_dado}")
        if dado_mas_alto > numero_del_dado:
            jugador = i
            dado_mas_alto = numero_del_dado
    print(f"Ha ganado el jugador {jugador}")
