from Personaje import Personaje


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

def jugar():

def menu():
    salir = False
    opcion = 0
    while not salir:
        print("1 → Jugar CPU")
        print("2 → Jugar 1vs1")
        print("3 → salir")

        print("Elige una opción")

        opcion = pedirNumeroEntero()

        if opcion == 1:
            jugar()
        elif opcion == 2:
            jugar2v2()
        elif opcion == 3:
            salir = True
        else:
            print("Introduce un número del 1 al 3")

menu()
print ("Fin")