#intervalo de numeros

print("Ingrese los limites del primer intervalo")
a=float(input("Ingrese el limite inferior: "))
b=float(input("Ingrese el limite superior: "))
print("Ingrese los limites del segundo intervalo")
c=float(input("Ingrese el limite inferior: "))
d=float(input("Ingrese el limite superior: "))
print("Ingrese los limites del tercer intervalo")
e=float(input("Ingrese el limite inferior: "))
f=float(input("Ingrese el limite superior: "))
x=float(input("Ingrese el numero a validar: "))
if x>a and x<b:
    print("El número se encuentra en el primer intervalo")
elif x>c and x<d:
    print("El número se encuentra en el segundo intervalo")
elif x>e and x<f:
    print("El número se encuentra en el tercer intervalo")
else:
    print("El número no se encuentra en ningun intervalo")