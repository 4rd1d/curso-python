from random import randint
print("JUEGOS DE DADOS (3)")
elena1 = randint(1,6)
elena2 = randint(1,6)
fernando1 = randint(1,6)
fernando2 = randint(1,6)
if elena1 + elena2 > fernando1 + fernando2:
    print(f"Elena ha sacado un {elena1} y un {elena2}. \n"
          f"Fernando ha sacado un {fernando1} y un {fernando2}. \n"
          f"Ha ganado Elena")
elif elena1 + elena2 < fernando1 + fernando2:
    print(f"Elena ha scado {elena1} y un {elena2}. \n"
          f"Fernando ha sacado {fernando1} y un {fernando2}. \n"
          f"Ha ganado Fernando.")
else:
    print("Han empatado")