"""Ejercicio 1
Programa plano cartesiano"""

print("-----------------------")
print("-----PLANO CARTESIANO--------")
print("-----------------------")

#input 
x = int(input("Digite la cordenada x: "))
y = int(input("Digite la cordenada y: "))

#processing
if x>=0 and y>=0:
    print("las coordenadas:" + "(" +str(x)+"," + str(y) +")" + " se encuentra en el CUADRANTE 1.")
else:
    if x<=0 and y<=0:
        print("Las coordenadas: " + "(" +str(x)+"," + str(y) + ")" + " se encuentran en el CUADRANTE 2.")
    else:
        if x<=0 and y<=0:
            print("Las coordenadas: " + "(" +str(x)+"," + str(y) + ")" + " se encuentran en el CUADRANTE 3.")
        else:
            if x>=0 and y<=0:
                print("Las coordenadas: " + "(" +str(x)+"," + str(y) + ")" + " se encuentran en el CUADRANTE 4.")

    