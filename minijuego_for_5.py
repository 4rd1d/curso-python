from random import randint
print("EL DADO MAS ALTO")
cantidad_dados = int(input("Numero de dados: "))
if cantidad_dados <= 0:
    print("¡Imposible!")
else:
    dado_mas_alto = 1
    print("Dados: ", end=" ")
    for i in range(cantidad_dados):
        numero_dado = randint(1, 6)
        print(f"{numero_dado}", end=" ")
        if numero_dado > dado_mas_alto:
            dado_mas_alto = numero_dado
    print()
    print(f"El dado mas alto es {dado_mas_alto}")


