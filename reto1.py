#ENTRADAS = VARIABLES=REFERENCIAS EN MEMORIA
nivelagua= None 
nivelagua=int(input("Digite el nivel del agua: "))


#PROCESO
if(nivelagua>=0 and nivelagua<20):
    print(f'el nivel de agua es {nivelagua} y este es bajo')
elif(nivelagua>=20 and nivelagua<400):
    print(f'el nivel de agua es {nivelagua} operando normalmente')
elif(nivelagua>=400):
    print(f'el nivel de agua es {nivelagua} peligro ')
else:
    print("el nivel del agua no es valido")


#SALIDA 