print("JUEGO DE DADOS (2)")
from random import choice
carmen1 = choice(range(1,7))
carmen2 = choice(range(1,7))
david1 = choice(range(1,7))
david2 = choice(range(1,7))

if carmen1 + carmen2 > david1 + david2:
    print(f"Carmen ha sacado un {carmen1} y un {carmen2} \n"
          f"David ha sacado un {david1} y un {david2} \n"
          f"Ha ganado Carmen")
elif carmen1 + carmen2 < david1 + david2:
    print(f"Carmen ha sacado un {carmen1} y un {carmen2} \n"
          f"David ha sacado un {david1} y un {david2} \n"
          f"Ha ganado david")
elif carmen1 + carmen2 == david1 + david2:
    if max(carmen1,carmen2) > max(david1,david2):
        print(f"Carmen ha sacado un {carmen1} y un {carmen2} \n"
              f"David ha sacado un {david1} y un {david2} \n"
              f"Ha ganado Carmen")
    elif max(carmen1,carmen2) < max(david1,david2):
        print(f"Carmen ha sacado un {carmen1} y un {carmen2} \n"
              f"David ha sacado un {david1} y un {david2} \n"
              f"Ha ganado David")
    else:
        print("Han empatado")
