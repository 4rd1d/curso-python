print("CALCULO DEL INDICE DE MASA CORPORAL IMC")
peso = int(input("Cuanto pesa?: "))
metro = float(input("Cuanto mide en metros"))
imc = peso // metro**2
print(f"Su IMC es {imc}")
print("un IMC muy alto indica obesidad. Los valores normales de IMC estan entre 20 y 25 \n "
      "peros esos lkimites dependen de la edad , del sexo, de la constitucion fisica,etc")
