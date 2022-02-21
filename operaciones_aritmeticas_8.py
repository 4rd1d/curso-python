print("CONVERTIDOR DE A GRUESAS Y DOCENAS")
entero = int(input("Escriba una cantidad (entera): "))

gruesas = entero // 144 # 85
docenas = (entero % 144) // 12 # 8
unidades = entero % 12

print(f"{entero} unidades son {gruesas} gruesas, {docenas} docenas y {unidades} unidades.")