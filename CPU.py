from random import random
from Manu import jugar, personajeCPU
import os
import random

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

def personaje1(p1,p2):
    while True:
        if p2.getVida() > 0:
            opcion = int(input("Elige ataque → "))
            if opcion == 0:
                p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
            elif opcion == 1:
                p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
            elif opcion == 2:
                p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
            elif opcion == 3:
                p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
                vidasJugadores(p1,p2)
            else:
                print("No has elegido ningún ataque ")

def lucha(p1,p2):
    os.system("cls")
    ronda = 0
    while p1.getVida() > 0 and p2.getVida() > 0:
        ronda = ronda + 1
        for i in range(len(p1.getTecnicas())):
            print(i, " → ", p1.getTecnicas()[i].getNombre())
        personaje1(p1,p2)
        os.system("cls")
        CPU(p1,p2)

def personajeCPU(p1):
    cpu = random.choice(personajes)
    os.system("cls")
    print("Juegas contra ", cpu.getNombre())
    getPersonajeElegido(cpu)
    lucha(p1,cpu)


def vidasJugadores(p1,p2):
    print("Vda de tu jugador → ", p1.getVida)
    print("Vida de la CPU → ", p2.getVida)

def getPersonajeElegido(personaje):
    print(personaje.getNombre())
    print(personaje.getVida())
    for i in personaje.getTecnicas():
        print("El daño es de ", i.getDano())

def confirmacionJugador(personaje):
    getPersonajeElegido(personaje)
    opcion = input("¿Quieres este jugador? (s/n) ")
    if opcion == "s":
        personajeCPU(personaje)
    else:
        os.system("cls")
        jugar()