from tokenize import PseudoExtras
from traceback import print_tb
from Personaje import Personaje
import os
from Tecnicas import Tecnica

personajes =[]

class bcolors:
    verde = '\033[92m'
    rojo = '\033[91m'
    normal = '\033[0m'

def pedirNumeroEntero():
    correcto = False;
    num=0;
    while(not correcto):
        try:
            num = int(input(""))
            correcto = True;
        except ValueError:
            print("Error, introduce un numero entero")
    return num
def tecnicasDefault():
    global t1,t2,t3,t4
    t1 =Tecnica("t1", 50)
    t2 = Tecnica("t2", 100)
    t3 = Tecnica("t3", 500)
    t4 = Tecnica("t4", 1000)
    

def personajesDefault():
    global p1,p2,p3,p4
    p1 = Personaje("TATIANA", 4000) 
    p2 = Personaje("EDUARD", 4000) 
    p3 = Personaje("VIOLETA", 4000) 
    p4 = Personaje("LUCAS", 4000) 
    p1.setTecnicas([t1,t2,t3,t4])
    p2.setTecnicas([t1,t2,t3,t4])
    p3.setTecnicas([t1,t2,t3,t4])
    p4.setTecnicas([t1,t2,t3,t4])
    personajes.append(p1)
    personajes.append(p2)
    personajes.append(p3)
    personajes.append(p4)


class bcolors:
    verde = '\033[92m'
    rojo = '\033[91m'
    normal = '\033[0m'



def menu():
    salir = False
    opcion = 0
    while not salir:
        print("1 → Jugar CPU")
        print("2 → Jugar 1vs1")
        print("3 → Crear Personaje")
        print("4 → salir")

        print("Elige una opción")

        opcion = pedirNumeroEntero()
        os.system("cls")

        if opcion == 1:
            jugar()
        elif opcion == 2:
            jugar1v1()
        elif opcion == 3:
            crearPersonaje()
        elif opcion == 4:
            salir = True
        else:
            print("Introduce un número del 1 al 3")

tecnicasDefault()
personajesDefault()
menu()

