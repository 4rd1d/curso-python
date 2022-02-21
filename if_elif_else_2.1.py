print("DVISOR DE NUMEROS")
n1 = int(input("Escriba el dividendo: "))
n2 = int(input("Escriba el divisor: "))

if n2 ==0:
    print("No se puede dividir por cero")
elif n1 % n2 == 0:
    print(f"La division es exacta. Cociente: {n1 // n2}")
else:
    print(f"La diviosn no es exacta. Cociente: {n1//n2} Resto: {n1%n2}")
0