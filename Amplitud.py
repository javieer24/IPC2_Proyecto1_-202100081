class Amplitud:
    # Atributos
    amplitud: float
    dato: float

    # Constructor
    def __init__(self, amplitud, dato=0):
        self.amplitud = amplitud
        self.dato = dato

    # Métodos

    def getAmplitud(self):
        return self.amplitud

    def getDato(self):
        return self.dato

    def print(self):
        print(self.amplitud, self.dato)
        