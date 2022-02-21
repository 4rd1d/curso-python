
print("ECUACION AX² + bx + c = 0") # x = -b ± (b **2 - 4ac) ** 1/2
a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))
c = float(input("Escriba el valor del coeficiente c: "))

if a == 0 and b == 0 and c == 0:
    print("Todos los numeros son solucion")
elif a == 0 and b == 0 and c != 0:
    print("Sin solucion")
elif a == 0 and b != 0 and c != 0:
    print(f"Una solucion: {-c/b}")
elif a != 0 and b != 0 and c != 0:
    x = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
    y = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)
    if complex == type(x) and complex == type(y):
        print("Sin solucion real")
    elif x != 0 and y != 0 and x != y:
        print(f"Dos soluciones: {x,y}")
    elif x == y:
        print(f"Una solucion: {x or y} ")


