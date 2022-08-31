edad=int(input("Digite la edad:  "))

#proceso
if(edad>=0 and edad <14):
    print(f' la edad es:{edad} y es menor ')
elif(edad>=14 and edad <28):
    print(f' la edad es:{edad} y es joven ')
elif(edad>=28 and edad <60):
    print(f' la edad es:{edad} y es adulto ')
elif(edad>=60 and edad <150):
    print(f' la edad es:{edad} y es adulto mayor ')
    