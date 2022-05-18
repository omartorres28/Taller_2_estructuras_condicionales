"""Ejercicio 2
Programa prestamos"""

print("--------")
print("------Valor de ingresos --------")
print("--------")

#input 
Ingresos=int(input("Ingrese el numero de sus ingresos "))
Deudas=int(input("Ponga 0 si no tiene deudas o ponga 1 si tiene deudas "))

#processing
if Deudas==0 and Ingresos>945200:
    print(" Aprobado el prestamo ")
else:
     print(" denegado ")