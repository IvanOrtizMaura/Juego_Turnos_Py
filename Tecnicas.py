class Tecnica:
    nombre = "";
    daño = 0;
    
    def __init__(self, nombre, daño):
        self.nombre = nombre 
        self.daño = daño

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDano(self):
        return self.daño
    def setDano(self, daño ):
        self.daño = daño 