# Piedra, papel o tijera

import random

print("--------------------------------------------")
print("-----------Piedra, papel o tijera-----------")
print("--------------------------------------------")

print("1 Corresponde a piedra")
print("2 Corresponde a papel")
print("3 Corresponde a tijera")

# input

j = int(input("¿Qué escoges?: "))
    
# processing

m = random.randint(1,3)

if (j == 1):
    if (m == 1 ):
        print("Empate")
        print("Elegiste piedra y la máquina sacó piedra")
    elif (m==2):
        print("Lo siento, perdiste")
        print("Elegiste piedra y la máquina sacó papel")
    else:
        print("Felicidades, ganaste")
        print("Elegiste piedra y la máquina sacó tijera")

        
if (j == 2):
    if (m == 1):
        print("Felicidades, ganaste")
        print("Elegiste papel y la máquina sacó piedra")
    elif (m == 2):
        print("Empate")
        print("Elegiste papel y la máquina sacó papel")
    else:
       print ("Lo siento, perdiste")
       print("Elegiste papel y la máquina sacó tijera")


if (j == 3):
    if ( m == 1):
        print("Lo siento, perdiste")
        print("Elegiste tijera y la máquina sacó piedra")
    elif ( m ==2):
        print("Felicidades, ganaste")
        print("Elegiste tijera y la máquina sacó piedra")
    else:
        print("Empate")
        print("Elegiste tijera y la máquina sacó tijera")

if (j > 3):
    print("Ingresaste una opcion inválida, revisa las opciones")