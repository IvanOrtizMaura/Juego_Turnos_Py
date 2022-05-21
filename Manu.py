from itertools import tee
from pickle import TUPLE3
from Personaje import Personaje
import os
from Tecnicas import Tecnica
import random


personajes =[]
tecnincas = []
# Creo variables con los colores para destacar las vidas y los daños de los ataques
class bcolors:
    verde = '\033[92m'
    rojo = '\033[91m'
    normal = '\033[0m'
# Comprobar que el usuaro a elegido una opcion del menu 
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
# En este método creo las tecnicas por defecto de los personajes 
def tecnicasDefault():
    global t1,t2,t3,t4
    t1 =Tecnica("t1", 50)
    t2 = Tecnica("t2", 100)
    t3 = Tecnica("t3", 500)
    t4 = Tecnica("t4", 1000)
    tecnincas.append(t1)
    tecnincas.append(t2)
    tecnincas.append(t3)
    tecnincas.append(t4)
    
# Creo los personajes por defecto del juego 
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


# ***********************************************************************************
# *                                Crear Nuevo Personaje                            *
# ***********************************************************************************
# Compruebo la vida del personaje que ha creado el usuario
def comprobarVidaNuevoPersonaje(vida, nombre):
    if vida > 8000:
        print("Intoduce una vida dentro del rango",bcolors.verde, "(8000 HP)", bcolors.normal)
        vida = int(input ("Introduce la vida de " + nombre + " → "))
        return vida
    else:
        return vida

# Le pido los datos del personaje que está creando
def crearPersonaje():
    eleccionTecnica = []
    nombre = input("Introduce el nombre de tu Nuevo Personaje → ")
    vida = int(input("Introduce la vida que quieres para "  + nombre + " → "))
    comprobarVidaNuevoPersonaje(vida, nombre)
    for i in range(len(tecnincas)):
        print(i, "El daño es de ", bcolors.rojo, tecnincas[i].getDano(), bcolors.normal)
    for i in range(0,4):
        eleccion = int(input("Elije las tecnicas que quieras para " + nombre + " → "))
        eleccionTecnica.append(tecnincas[eleccion])        

    p1 = Personaje(nombre, vida)
    p1.setTecnicas(eleccionTecnica)
    personajes.append(p1)


# ***********************************************************************************
# *                                    Jugar 1 vs 1                                 *
# ***********************************************************************************
# Enseño al usuario la vida de los jugadores
def vidasJugadores(p1,p2):
    if p1.getVida() > 0:
         print("Vida de tu Jugador 1 → ", bcolors.verde, p1.getVida(), bcolors.normal)
    else:
        print("Vida de tu Jugador 1 → ", bcolors.rojo, p1.getVida(), bcolors.normal)
    if p2.getVida() > 0:
        print("Vida de Jugador 2 → ",bcolors.verde, p2.getVida(), bcolors.normal)
    else:
         print("Vida de Jugador 2 → ",bcolors.rojo, p2.getVida(), bcolors.normal)

# Le pido al jugador 1 que ataque quiere usar en su turno 
def turnoPesonaje1(p1,p2):
    print("*************************************************")    
    print("*                 Turno Jugador 1               *")
    print("*************************************************")
    for i in range(len(p1.getTecnicas())):
            print(i, " → ", p1.getTecnicas()[i].getNombre())

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
         print("No has elegido ningún ataque")

            
# Le pido al jugador 2 que ataque quiere usar en su turno 
def turnoPersonaje2(p1,p2):
    print("*************************************************")    
    print("*                Turno Jugador 2                *")
    print("*************************************************")
    for i in range(len(p1.getTecnicas())):
            print(i, " → ", p1.getTecnicas()[i].getNombre())
        
    opcion = int(input("Elige ataque → "))
    if opcion == 0:
        p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
        vidasJugadores(p1,p2)
    elif opcion == 1:
        p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
        vidasJugadores(p1,p2)
    elif opcion == 2:
        p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
        vidasJugadores(p1,p2)
    elif opcion == 3:
        p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
        vidasJugadores(p1,p2)
    else:
        print("No has seleccionado ningún ataque")

# Es el metodo principal del 1 vs 1
def lucha1v1(p1,p2):
    ronda = 0 
    while p1.getVida() > 0 and p2.getVida() > 0:
        ronda = ronda + 1 
        print("*************************************************")     
        print("*                     ROUND ",ronda,"                 *")
        print("*************************************************")
        turnoPesonaje1(p1,p2)
        os.system("cls")
        turnoPersonaje2(p1,p2)
    else:
        if p1.getVida() <= 0:
            os.system("cls")
            print("*************************************************")     
            print("*                 Ha ganado Jugador 2           *")
            print("*************************************************") 
        else:
            os.system("cls")
            print("*************************************************")     
            print("*                 Ha ganado Jugador 1           *")
            print("*************************************************")   
        
# Le enseño los ataques que tiene ese personaje y le pregunto al usuario si esta conforme con ese personaje
def confirmacionJugador2(p1,p2):
    getPersonajeElegido(p2)
    opcion = input("¿Quieres a este personaje? (s/n) ")
    if opcion == 's':
        lucha1v1(p1,p2)
    else:
        eleccionPersonaje2()

# Le doy a elegir al usuairo que prsonaje quiere usar para la pelea 
def eleccionPersonaje2(p1):
    print("******************************")
    print("Estas en seleccion de personaje 2 ")
    bandera = True
    for i in range(len(personajes)):
        print(i,personajes[i].getNombre())
    while bandera:
        opcion = int(input("Introduce el número del personaje → "))
        if opcion > len(personajes):
            print("Error..!")
        else:
            bandera = False
    opcion = personajes[opcion]
    print("Has elegido a ", opcion.getNombre())
    confirmacionJugador2(p1,opcion)

    
# Le muestro los ataques del personaje 
def getPersonajeElegido(personaje):
    print(bcolors.verde ,personaje.getVida(),bcolors.normal, " HP")
    for i in personaje.getTecnicas():
        print("El daño es de ", bcolors.rojo, i.getDano(), bcolors.normal)

# Le pregunto al usuario si esta conforme con el personaje que ha elegido
def confirmacionJugador(personaje):
    getPersonajeElegido(personaje)
    opcion = input("Quieres este jugador? (s/n) ")
    if opcion == 's':
        eleccionPersonaje2(personaje)
    else:
        jugar1v1()
# Es el método principal del 1 vs 1
def jugar1v1():
    bandera  = True
    for i in range(len(personajes)):
        print( i, personajes[i].getNombre() )
    while bandera:
        opcion = int(input("Introduce el número de un personaje → "))
        if opcion > len(personajes):
            print("Introduce un número dentro del rango de los personajes que salen por pantalla")
        else:
            bandera = False
    opcion = personajes[opcion]
    print("Tu personaje es ", opcion.getNombre())
    confirmacionJugador(opcion)


# ***********************************************************************************
# *                                  Clase Jugar CPU                                *
# ***********************************************************************************
def getPersonajeElegido(personaje):
    print( personaje.getNombre())
    print(bcolors.verde,personaje.getVida(), bcolors.normal)
    for i in personaje.getTecnicas():
        print("El daño es de ",bcolors.rojo, i.getDano(),bcolors.normal)


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
    bandera = True
    while bandera:
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
        else:
            
            bandera: False
        

def CPU(p1,p2):
    bandera = True
    while bandera:
        
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
        else:
            bandera = False
    


def luchaCPU(p1,p2):
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
    else:
        if p1.getVida() <= 0:
            os.system("cls")
            print("*************************************************")     
            print("*                    Ha ganado CPU              *")
            print("*************************************************") 
        else:
            os.system("cls")
            print("*************************************************")     
            print("*                 Ha ganado Jugador 1           *")
            print("*************************************************")
              
        

def personajeCPU(p1):
    cpu = random.choice(personajes)
    os.system("cls")
    print ("Juegas contra ", cpu.getNombre())
    getPersonajeElegido(cpu)
    luchaCPU(p1,cpu)


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


# ***********************************************************************************
# *                                        Menu                                     *
# ***********************************************************************************
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