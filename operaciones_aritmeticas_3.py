print("CONVERTIR DE PIES Y PULGADAS A CENTIMETROS")
pies = int(input("Escriba uina cantidad de pies: "))
pulgadas = int(input("Escriba una cantidad de pulgadas: "))

total = float(pies*30.48+pulgadas*2.54)
print(f"{pies} pies y {pulgadas} son {total} cm")


