'''
Ejercico 4:
Hacer un prgoama para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia
'''
import math
radio=float(input("Ingrese el radio del circulo --> "))
area=math.pi*radio**2
longitud=2*3.14*radio
print(f"El área del circulo es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")
