print("ECUACION AX + B = 0") # X = -B / A
a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))

if a == 0 and b > 0:
    print("La ecuacion no tiene solucion")
elif a != 0 and b != 0:
    print(f"La ecuacion tiene una solucion {-b/a}")
else:
    print("Todos los numeros son solucion")
