print("CALCULO DE AREAS")
print("Elija una figura geometrica: \n"
      "a) Triangulo \n"
      "b) Circulo")
figura = str(input("Que figura quiere calcular (Escriba T o C)?: "))
if "T"== figura or "t"== figura:
    base = float(input("Escriba la base: "))
    altura = float(input("Escriba la altura: "))
    print(f"Un triangulo de base {base} y altura {altura} tiene un area {(base*altura)/2}")
elif "C" == figura or "c" == figura:
    circulo = float(input("Escriba el radio: "))
    print(f"Un circulo de radio {circulo} tiene una area de {3.141592 * circulo**2}")