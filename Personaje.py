class Personaje():
    nombre ="";
    vida = 0;
    clase = "";
    tecnica ="";
    def __init__(self, nombre, vida, ):
        self.nombre = nombre;
        self.vida = vida;
        self.tecnica = [];
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre

    def getVida(self):
        return self.vida
    def setVida(self, vida):
        self.vida = vida

    def getTecnicas(self):
        return self.tecnica
        
    def setTecnicas(self, tecnicas):
        self.tecnica = tecnicas

    def getTecnicasNombre(self):
        nombreTecnica = []
        for i in self.tecnica:
            nombreTecnica.append(i.getNombre())
        return nombreTecnica