#descuento

valor=int(input("Ingrese el valor del artículo para ver si aplica descuento sin puntos ni comas: "))
if valor>=150000:
    b=valor*0.05
    print("El producto aplica para descuento del 5% por lo tanto su valor queda en $",valor-b)
else:
    print("El producto no aplica para descuento del 5% por lo tanto su valor queda en $",valor) 