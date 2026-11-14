#numero mayor
a=int(input("Ingrese el primer numero "))
b=int(input("Ingrese el Segundo numero "))
c=int(input("Ingrese el tercer numero "))
d=int(input("Ingrese el cuarto numero "))

if a>b and a>c and a>d:
    print("El numero ",a, " es mayor que " ,b, ", ",c, " y ",d)
elif b>a and b>c and b>d:
    print("El número ",b, " es mayor que ",a, ", ",c, " y ",d)
elif c>a and c>b and c>d:
    print("El número ",c, " es mayor que ",a, ", ",b, " y ",d)
else:
    print("El número ",d, " es mayor que ",a, ", ",b, " y ",c)