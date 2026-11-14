#promedio Notas

print("Ingrese las notas del estudiante entre 0.0 y 5.0")
a=float(input("Ingrese la primera nota: "))
b=float(input("Ingrese la segunda nota: "))
c=float(input("Ingrese la tercera nota: "))
d=float(input("Ingrese la cuarta nota: "))
e=float(input("Ingrese la quinta nota: "))
pr=(a+b+c+d+e)/5
if pr<3.5:
    print("Usted saco ", pr, " en el promedio de notas por lo que reprobo el curso")
else:
    print("Usted saco ", pr, " en el promedio de notas por lo que aprobo el curso")