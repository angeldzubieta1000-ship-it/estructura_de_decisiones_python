# Descuento de productos

precio_real=int(input("Ingrese el precio real del producto sin puntos ni comas: "))
tipo_producto=str(input("Ingrese el tipo de producto ( T para textil, E para electrodomestico, C para elementos de cocina, V para videojuego y O para otro tipo de producto: "))
if tipo_producto=='t' or tipo_producto=='T':
    print("El producto no se encuentra con descuento por lo que el valor a pagar sera $",precio_real)
elif tipo_producto=='e' or tipo_producto=='E':
    descuento=precio_real*0.037
    precio_final=precio_real-descuento
    print("El producto cuenta con el 3.7% de descuento por lo que el valor a pagar sera $",precio_final)
elif tipo_producto=='c' or tipo_producto=='C':
    descuento=precio_real*0.042
    precio_final=precio_real-descuento
    print("El producto cuenta con el 4.2% de descuento por lo que el valor a pagar sera $",precio_final)
elif tipo_producto=='v' or tipo_producto=='V':
    descuento=precio_real*0.078
    precio_final=precio_real-descuento
    print("El producto cuenta con el 7.8% de descuento por lo que el valor a pagar sera $",precio_final)
else:
    print("El producto no se encuentra con descuento por lo que el valor a pagar sera $",precio_real)