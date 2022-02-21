from random import randint
print("TIRADA DE DADOS")
dado = int(input("Numero de dados: "))
if dado <= 0:
    print("Imposible")
else:
    print("Dados: ", end=" ")
    for dado in range(1, dado+1):
        print(randint(1, dado), end=" ")
