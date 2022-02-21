from random import choice
print("JUEGO DE DADOS")
alberto = choice(range(1,7))
barbara = choice(range(1,7))

if alberto > barbara:
    print(f"Alberto ha sacado: {alberto} \n"
          f"Barbara ha sacado: {barbara} \n"
          f"Ha gandado Alberto")
elif alberto < barbara:
    print(f"Alberto ha sacado un: {alberto} \n"
          f"Barbara ha sacado un: {barbara} \n"
          f"Barbara ha gando")
else:
    print(f"Alberto ha sacado un: {alberto} \n"
            f"barbara ha sacado un: {barbara} \n"
            f"Han empatado")
