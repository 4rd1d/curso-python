print("PAR E IMPAR 4")
n1 = int(input("Ecriba un numero par: "))

if n1 % 2== 0: # abarca n2 impar
    n2 = int(input("Escriba un numero impar: "))
    if n2 % 2 !=0:
        print("Gracias por su colaboracion")
    else:
        print("No ha escrito un numero impar \n"
              "Ejecute de nuevo el programa para volver a intentarlo")
elif n1 % 2 != 0:
    print("No ha escrito un numero par ")
    n2 = int(input("Escriba un numero impar: "))
    if n2 % 2 == 0:
        print("No ha escrito un numero impar")
    else:
        print("Ejecute de nuevo el programa para volver a intentarlo")
