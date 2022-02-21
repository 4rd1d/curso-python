from random import randint
print("TIRADA DE DADOS")
jugadores = int(input("Numero de jugadores: "))
if jugadores <= 1:
    print("¡Imposible!")
else:
    for i in range(1, jugadores+1):
        print(f"Jugado {i}: {randint(1, 6)}")
