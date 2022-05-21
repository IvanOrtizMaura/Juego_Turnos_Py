# ***********************************************************************************
# *                                Crear Nuevo Personaje                            *
# ***********************************************************************************
def comprobarVidaNuevoPersonaje(vida, nombre):
    if vida > 8000:
        print("Intoduce una vida dentro del rango",bcolors.verde, "(8000 HP)", bcolors.normal)
        vida = int(input ("Introduce la vida de " + nombre + " → "))
        return vida
    else:
        return vida


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