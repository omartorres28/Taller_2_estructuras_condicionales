"""Ejecicio 4
Programa para calcular el IMC de una persona"""

print("--------------------")
print("---programa para calcular su estado de peso ---")
print("--------------------")

#input
peso=int(input("Digite su peso: "))
altura=int(input("Digite su altura en numeros enteros"))

#processing
imc= peso/altura**2

if imc<16:
    print("criterio ingreso al hospital")
elif imc>=16 and imc<=17:
    print("Infrapeso")
elif imc>=17 and imc<=18:
    print("Bajo peso")
elif imc>=18 and imc<=25:
    print("Peso normal")
elif imc>=25 and imc<=30:
    print("Sobrepeso")
elif imc>=30 and imc<=35:
    print("Sobrepeso cronico")
elif imc>=35 and imc<=40:
    print("obesidad premorbida")
elif imc>=40:
    print("Obesidad morbida") 
else:
    print("valor no valido")



sexoanal= altura/peso
print(sexoanal,"que rico hijueputa")