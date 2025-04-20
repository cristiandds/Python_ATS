'''
Ejercicio 5:
-Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente pro su compra
'''
precio=float(input("Ingrese el monto a pagar --> S/. "))
descuento=0.15*precio
precio_final= precio -descuento
print(f"El precio final a pagar es de S/: {precio_final:.2f}")