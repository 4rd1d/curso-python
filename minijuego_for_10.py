from random import randint
print("DADOS IGUALES")
cantidad_dado = int(input("Numero de dados: "))
if cantidad_dado <= 1:
    print("IMPOSIBLE")
else:
    cuenta = 0
    print("Dados: ", end=" ")
    for i in range(cantidad_dado):
        dado = randint(1, 6)
        print(dado, end=" ")
        cuenta = dado + 0
        if