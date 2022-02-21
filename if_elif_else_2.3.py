print("COMPARADOR DE AÑOS")
ano = int(input("En que año estamos: "))
ano_cualquiera = int(input("Escriba un año cualquiera: "))

if ano > ano_cualquiera:
    print(f"Desde el año {ano_cualquiera} han pasado {ano -ano_cualquiera} años")
elif ano < ano_cualquiera:
    if ano_cualquiera - ano == 1:
        print(f"Para llegar al año {ano_cualquiera} falta 1 año")
    else:
        print(f"Para llegar al año {ano} falta {ano_cualquiera - ano} años")
else:
    print("Son el mismo año")