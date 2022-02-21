print("PAR E IMPAR 2")
n1 = int(input("Escriba un numero par: "))

if n1 % 2 == 0:
    n2 = int(input("Escriba un numero impar: "))
    if n2 % 2 !=0:
        print("Gracias por su colaboracion")
    elif n2 % 2 ==0:
        print("No ha escrito un numero impar")
else:
    print("No ha escrito un numero par")



