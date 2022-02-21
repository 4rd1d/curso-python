from random import choice
print("PIEDRA, PAPEL, ... ¡TIJERA!")
piedra = 1
papel = 2
tijera = 3
ines = choice([piedra,papel,tijera])#123
juan = choice([piedra,papel,tijera])#123
if ines > juan:
    if piedra > tijera:#1 3
        print(f"Ines ha sacado piedra. \n"
              f"Juan ha sacado tijera. \n"
              f"Ha ganado Ines")
    elif papel > piedra:#2 1
        print(f"Ines ha sacado papel. \n"
              f"Juan ha sacado piedra. \n"
              f"Ha ganado Ines")
    elif tijera > papel:#3 2
        print(f"Ines ha sacado tijera. \n"
              f"Juan ha sacado papel. \n"
              f"Ha ganado Ines")
elif ines < juan:
    if piedra > tijera:#1 3
        print(f"Ines ha sacado tijera. \n"
              f"Juan ha sacado piedra. \n"
              f"Ha ganado Juan")
    elif papel > piedra:#2 1
        print(f"Ines ha sacado piedra. \n"
              f"Juan ha sacado papel. \n"
              f"Ha ganado Juan")
    elif tijera > papel:#3 2
        print(f"Ines ha sacado papel. \n"
              f"Juan ha sacado tijera. \n"
              f"Ha ganado Juan")
else:
    print("Han empatado")