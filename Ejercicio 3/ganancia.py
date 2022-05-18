"""Ejercicio 3 
Programa para calcular el precio de venta de un articulo"""

print("-------------------")
print("--------precio del articulo----------")
print("-------------------")

#input
precio_costo=float(input("Digite el precio costo del articulo"))

#processing
if precio_costo<3000:
   ganancia=0.15*precio_costo
else:
    if precio_costo<=6000:
        ganancia=500
    else: 
        ganancia=precio_costo*0.25
    precio_venta=precio_costo+ganancia

#output 
p=precio_costo+ganancia

print("El precio de venta del articulo de costo :"+str(precio_costo)+ " es:"+str(p))
