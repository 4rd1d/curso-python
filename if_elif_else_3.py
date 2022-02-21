print("PAR E IMPAR 3")
n1 = int(input("Escriba un numero par: "))
n2 = int(input("Escriba un numero impar: "))

if n1 % 2 != 0 and n2 % 2 == 0:
    print("No ha escrito un numero par \n "
        "No ha escrito un numero impar")
elif n1 % 2 == 0 and n2 % 2 == 0:
    print("No ha escrito un numero impar")
elif n1 % 2 !=0 and n2 % 2 !=0:
    print("No ha escrito un numero par")
elif n1 % 2 ==0 and n2 % 2 != 0:
    print("Gracias por su colaboracion")

