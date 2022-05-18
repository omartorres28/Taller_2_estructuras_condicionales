"""Ejecicio 5 
Programa para calcular el costo del agua"""

print("-------------------")
print("-----metros gastados----")
print("-------------------")

#input
metros_gastados=float(input("Ingrese los metros gastados: "))


#processing
if metros_gastados<=50:
    print(" Es igual a 10000 ")
elif metros_gastados<=200:
    costo_agua=10000+2000*(metros_gastados-50)
    print(costo_agua)
elif metros_gastados>200:
    costo_agua=10000+300*(metros_gastados-50)
    print(costo_agua)