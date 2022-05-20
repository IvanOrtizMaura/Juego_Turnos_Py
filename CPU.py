# def getPersonajeElegido(personaje):
#     print( personaje.getNombre())
#     print(bcolors.verde,personaje.getVida(), bcolors.normal)
#     for i in personaje.getTecnicas():
#         print("El daño es de ",bcolors.rojo, i.getDano(),bcolors.normal)

# def vidasJugadores(p1,p2):
#     if p1.getVida() > 0:
#         print("Vida de tu jugador → ", bcolors.verde, p1.getVida(), bcolors.normal)
#     else:
#         print("Vida de tu jugador → ", bcolors.rojo, p1.getVida(), bcolors.normal)
#     if p2.getVida() > 0:
#         print("Vida de CPU → ",bcolors.verde, p2.getVida(), bcolors.normal)
#     else:
#         print("Vida de CPU → ",bcolors.rojo, p2.getVida(), bcolors.normal)

# def personaje1(p1, p2):
#     bandera = True
#     while bandera:
#         if p2.getVida() > 0:
#             opcion = int(input("Elige ataque → "))
#             if opcion == 0:
#                 p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#                 break
#             elif opcion == 1:
#                 p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#                 break
#             elif opcion == 2:
#                 p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#                 break
#             elif opcion == 3:
#                 p2.setVida(p2.getVida() - p1.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#                 break
#             else:
#                 print("no has elegido ningun ataque")
#         else:
            
#             bandera: False
        

# def CPU(p1,p2):
#     bandera = True
#     while bandera:
        
#         if p2.getVida() > 0:
#             opcion = random.randint(0,3)
#             if opcion == 0:
#                 p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#                 break
#             elif opcion == 1:
#                 p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#                 break
#             elif opcion == 2:
#                 p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#                 break
#             elif opcion == 3:
#                 p1.setVida(p1.getVida() - p2.getTecnicas()[opcion].getDano())
#                 vidasJugadores(p1,p2)
#                 break
#             else:
#                 print("no has elegido ningun ataque")
#                 break
#         else:
#             bandera = False
    


# def lucha(p1,p2):
#     os.system("cls")
#     ronda = 0
#     while p1.getVida() > 0 and p2.getVida() > 0:
#         ronda = ronda +1 
#         print("*************************************************")     
#         print("*                     ROUND ",ronda,"                 *")
#         print("*************************************************")

#         for i in range(len(p1.getTecnicas())) :
#             print(i," → ", p1.getTecnicas()[i].getNombre())    
#         personaje1(p1,p2)
#         os.system("cls")
#         CPU(p1,p2)
#     else:
#         os.system("cls")
              
        

# def personajeCPU(p1):
#     cpu = random.choice(personajes)
#     os.system("cls")
#     print ("Juegas contra ", cpu.getNombre())
#     getPersonajeElegido(cpu)
#     lucha(p1,cpu)


# def confirmacionJufgador(personaje):
#     getPersonajeElegido(personaje)
#     opcion = input("¿Quiere este jugador? (s/n) ")
#     if opcion == "s":
#         personajeCPU(personaje)
#     else:
#         os.system("cls")
#         jugar()
    
# def jugar():
#     bandera = True
#     for i in range(len(personajes)):
#         print (i,personajes[i].getNombre() )
#     while bandera:
#         opcion =int(input("Introduce el numero de un personaje → "))
#         if opcion > len(personajes):
#             print("Error...")
#         else:
#             bandera = False
#     opcion = personajes[opcion]
#     print("Tu personaje es ", opcion.getNombre())
#     os.system("cls")
#     confirmacionJufgador(opcion)
