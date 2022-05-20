# def vidasJugadores(p1,p2):
#     if p1.getVida() > 0:
#          print("Vida de tu jugador → ", bcolors.verde, p1.getVida(), bcolors.normal)
#     else:
#         print("Vida de tu jugador → ", bcolors.rojo, p1.getVida(), bcolors.normal)
#     if p2.getVida() > 0:
#         print("Vida de CPU → ",bcolors.verde, p2.getVida(), bcolors.normal)
#     else:
#          print("Vida de CPU → ",bcolors.rojo, p2.getVida(), bcolors.normal)

# def turnoPesonaje1(p1,p2):
#     print("*************************************************")    
#     print("*                 Turno Jugador 1               *")
#     print("*************************************************")
#     for i in range(len(p1.getTecnicas())):
#             print(i, " → ", p1.getTecnicas()[i].getNombre())
#     bandera = True
#     while bandera:
#         if p2.getVida() > 0:
#             opcion = int(input("Elige ataque → "))
#             if opcion == 0:
#                 p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#             elif opcion == 1:
#                 p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#             elif opcion == 2:
#                 p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#             elif opcion == 3:
#                 p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#             else:
#                  print("No has elegido ningún ataque")
#         else:
#             bandera = False

            
# def turnoPersonaje2(p1,p2):
#     print("*************************************************")    
#     print("*                Turno Jugador 2                *")
#     print("*************************************************")
#     for i in range(len(p1.getTecnicas())):
#             print(i, " → ", p1.getTecnicas()[i].getNombre())
#     bandera = True
#     while bandera:
#         if p1.getVida() > 0:
#             opcion = int(input("Elige ataque → "))
#             if opcion == 0:
#                 p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#             elif opcion == 1:
#                 p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#             elif opcion == 2:
#                 p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#             elif opcion == 3:
#                 p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#             else:
#                 print("No has seleccionado ningún ataque")
#         else:
#             bandera = False
# def lucha(p1,p2):
#     ronda = 0 
#     while p1.getVida() > 0 and p2.getVida() > 0:
#         ronda = ronda + 1 
#         print("*************************************************")     
#         print("*                     ROUND ",ronda,"                 *")
#         print("*************************************************")
#         turnoPesonaje1(p1,p2)
#         os.system("cls")
#         turnoPersonaje2(p1,p2)
#     else:
#         os.system("cls")
        

# def confirmacionJugador2(p1,p2):
#     getPersonajeElegido(p2)
#     opcion = input("¿Quieres a este personaje? (s/n) ")
#     if opcion == 's':
#         lucha(p1,p2)
#     else:
#         eleccionPersonaje2()

# def eleccionPersonaje2(p1):
#     print("******************************")
#     print("Estas en seleccion de personaje 2 ")
#     bandera = True
#     for i in range(len(personajes)):
#         print(i,personajes[i].getNombre())
#     while bandera:
#         opcion = int(input("Introduce el número del personaje → "))
#         if opcion > len(personajes):
#             print("Error..!")
#         else:
#             bandera = False
#     opcion = personajes[opcion]
#     print("Has elegido a ", opcion.getNombre())
#     confirmacionJugador2(p1,opcion)

    

# def getPersonajeElegido(personaje):
#     print(bcolors.verde ,personaje.getVida(),bcolors.normal, " HP")
#     for i in personaje.getTecnicas():
#         print("El daño es de ", bcolors.rojo, i.getDano(), bcolors.normal)

# def confirmacionJugador(personaje):
#     getPersonajeElegido(personaje)
#     opcion = input("Quieres este jugador? (s/n) ")
#     if opcion == 's':
#         eleccionPersonaje2(personaje)
#     else:
#         jugar1v1()

# def jugar1v1():
#     bandera  = True
#     for i in range(len(personajes)):
#         print( i, personajes[i].getNombre() )
#     while bandera:
#         opcion = int(input("Introduce el número de un personaje → "))
#         if opcion > len(personajes):
#             print("Introduce un número dentro del rango de los personajes que salen por pantalla")
#         else:
#             bandera = False
#     opcion = personajes[opcion]
#     print("Tu personaje es ", opcion.getNombre())
#     confirmacionJugador(opcion)