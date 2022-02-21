print("CONVERTIDOR DE CM a KM, M y CM")
n = int(input("Escriba una distancia en centimetros: "))
if n > 0:
   # km = n // 100000
   # m = (n % 100000) // 100
    #cm = (n % 100000) % 100
    if n < 100:
        print(f"{n} centimetros son {n}")
    elif n > 99 and n <= 99999: # 100 n 99999
        m = n // 100
        cm = n % 100
        if m != 0 and cm != 0:
            print(f"{n} centimetros son {m} m {cm} cm")
        else:
            print(f"{n} centimetros son {m} m")
    elif n > 99999:
        km = n // 100000
        m = (n % 100000) // 100
        cm = (n % 100000) % 100
        if km != 0 and m != 0 and cm != 0:
            print(f"{n} centimetros son {km} km  {m} m {cm} cm")
        elif km != 0 and m != 0:
            print(f"{n} centimetros son {km} km {m} m ")
        elif km != 0 and cm != 0:
            print(f"{n} centimetros son {km} km {cm} cm")
        else:
            print(f"{n} centimetros son {km} km")
else:
    print("Escriba una distancia mayor que cero")
