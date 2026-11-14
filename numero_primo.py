# Numero primo

a=int(input("Ingrese un numero entre 0 y 20:"))
if a<0 or a>20:
    print("Numero invalido")
elif a==2 or a==3 or a==5 or a==7 or a==11 or a==13 or a==17 or a==19:
    print("El número es primo")
else:
    print("El numero no es primo")