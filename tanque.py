#Tanque de agua

a=int(input("Ingrese el valor del tanque actualmente: "))
if a<0:
    print("Opcion invalida")
elif a<450:
    print("La llave debe de estar abierta")
else:
    print("La llave debe de estar cerrada")