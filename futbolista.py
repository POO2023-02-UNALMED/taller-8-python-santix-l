from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista ):

    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol",  añosPracticando)
        self.golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self.piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self.golesMarcados

    def getTarjetasRojas(self):
        return self.tarjetasRojas

    def getPiernaHabil(self):
        return self.piernaHabil

    def setGolesMarcados(self, golesMarcados):
        self.golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self.tarjetasRojas = tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self.piernaHabil = piernaHabil

    def __str__(self):
        return "Mi nombre es " + self.getNombre() + " soy profesional en el deporte " + self.getDeporte() + " Tengo " + str(self.getEdad()) + " años de edad y llevo " + str(self.getAñosPracticando()) + " años en el deporte"