from cgitb import reset
from Personaje import Personaje
import os
from Tecnicas import Tecnica
import random
from colorama import Fore, init,Cursor

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

def getPersonajeElegido(personaje):
    print(personaje.getNombre())
    print(personaje.getVida())
    for i in personaje.getTecnicas():
        print("El daño es de ",i.getDano())

def vidasJugadores(p1,p2):
    if p1.getVida() > 0:
        print("Vida de tu jugador → ", bcolors.verde, p1.getVida(), bcolors.normal)
    else:
        print("Vida de tu jugador → ", bcolors.rojo, p1.getVida(), bcolors.normal)
    if p2.getVida() > 0:
        print("Vida de CPU → ",bcolors.verde, p2.getVida(), bcolors.normal)
    else:
        print("Vida de CPU → ",bcolors.rojo, p2.getVida(), bcolors.normal)

def personaje1(p1, p2):
    while True:
        if p2.getVida() > 0:
            opcion = int(input("Elige ataque → "))
            if opcion == 0:
                p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
                break
            elif opcion == 1:
                p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
                break
            elif opcion == 2:
                p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
                break
            elif opcion == 3:
                p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
                break
            else:
                print("no has elegido ningun ataque")
        

def CPU(p1,p2):
    while True:
        if p2.getVida() > 0:
            opcion = random.randint(0,3)
            if opcion == 0:
                p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
                break
            elif opcion == 1:
                p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
                break
            elif opcion == 2:
                p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
                break
            elif opcion == 3:
                p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
                break
            else:
                print("no has elegido ningun ataque")
                break

def lucha(p1,p2):
    os.system("cls")
    ronda = 0
    while p1.getVida() > 0 and p2.getVida() > 0:
        ronda = ronda +1 
        print("*************************************************")
        print("*                     ROUND ",ronda,"                 *")
        print("*************************************************")

        for i in range(len(p1.getTecnicas())) :
            print(i," → ", p1.getTecnicas()[i].getNombre())    
        personaje1(p1,p2)
        os.system("cls")
        CPU(p1,p2)
        
        

def personajeCPU(p1):
    cpu = random.choice(personajes)
    os.system("cls")
    print ("Juegas contra ", cpu.getNombre())
    getPersonajeElegido(cpu)
    lucha(p1,cpu)


def confirmacionJufgador(personaje):
    getPersonajeElegido(personaje)
    opcion = input("¿Quiere este jugador? (s/n) ")
    if opcion == "s":
        personajeCPU(personaje)
    else:
        os.system("cls")
        jugar()


def jugar():

    bandera = True
    for i in range(len(personajes)):
        print (i,personajes[i].getNombre() )
    
    while bandera:
        opcion =int(input("Introduce el numero de un personaje → "))
        if opcion > len(personajes):
            print("Error...")
        else:
            bandera = False
    opcion = personajes[opcion]
    print("Tu personaje es ", opcion.getNombre())
    
    os.system("cls")
    confirmacionJufgador(opcion)

    
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

