#Intervalo

a=int(input("Ingrese el valor minimo del intervalo: "))
b=int(input("Ingrese el valor maximo del intervalo: "))
c=int(input("Ingrese el número a validar: "))
if c>=a and c<=b:
    print("El número se encuentra en el rango")
else:
    print("El número no se encuentra en el rango")