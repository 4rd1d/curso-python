from random import randint
print("JUEGO DEL QUINCE")
gloria1 = randint(1, 10)
gloria2 = randint(1, 10)
gloria3 = randint(1, 10)
hector1 = randint(1, 10)
hector2 = randint(1, 10)
hector3 = randint(1, 10)

if gloria1 + gloria2 + gloria3 < 15 and hector1 + hector2 + hector3 < 15:
    if gloria1 + gloria2 + gloria3 > hector1 + hector2 + hector3:
        print(f"Gloria ha sacado un {gloria1}, un {gloria2} y un {gloria3}. \n"
              f"Hector ha sacado un {hector1}, un {hector2} y un {hector3}. \n"
              f"Ha ganado Gloria")
    elif gloria1 + gloria2 + gloria3 < hector1 + hector2 + hector3:
        print(f"Gloria ha sacado un {gloria1}, un {gloria2} y un {gloria3}. \n"
              f"Hector ha sacado un {hector1}, un {hector2} y un {hector3}. \n"
              f"Ha ganado Hector")
    else:
        print("Han empatado")
else:
    print("No ha ganado nadie")