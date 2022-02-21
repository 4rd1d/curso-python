print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")
s = int(input("Escriba cantidad e segundos: "))

horas = s // 3600
minutos = (s % 3600) // 60
segundos = s % 60
print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos} segundos")
