print("COMPROBADOR DE AÑOS BISIESTOS")
ano = int(input("Escriba un año y le dire si es bisiesto: "))

if ano % 4 == 0 or ano % 400 == 0:
    if ano % 400 == 0:
        print(f"El año {ano} es un año bisiesto porque es multiplo de 400")
    elif ano % 100 == 0:
        print(f"El año {ano} no es un año bisiesto porque es multiplo de 100 sin ser multiplo de 400")
    elif ano % 4 == 0:
        print(f"El año {ano} es un año bisiesto porque es multiplo de 4 sin ser multiplo de 400")
else:
    print(f"El ano {ano} no es un alo bisiesto")

