mes_dig=input("Digite el mes que desea evaluar ")
mes=mes_dig.lower()

if(mes=='enero' or mes=='febrero' or mes=='marzo'):
    print(f'estamos en invierno por se {mes}')
elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    print(f'estamos en primavera por se {mes}')
elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print(f'estamos en verano por se {mes}')
elif(mes=='octubre' or mes=='noviembre' or mes=='diciembre'):
    print(f'estamos en otoño por se {mes}')
else:
    print("mes no valido")

    