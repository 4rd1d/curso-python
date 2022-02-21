print("CONVERTIDOR DE GRADOS FAHRENHEIT A GRADOS CELSIUS")
f = float(input("Escriba una temperatura en grados fahrenheit: "))

c = float((f-32)/1.8)
print(f"{f}ºF son {round(c,1)}ºC")