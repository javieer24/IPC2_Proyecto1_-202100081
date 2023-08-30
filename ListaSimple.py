from nodo import Nodo
from graphviz import Graph

class ListaSimple():
    id = 0
    def __init__(self):
        self.primer_nodo = None
        self.size = 0

    def get_inicio(self):
        return self.primer_nodo

    def esta_vacia(self):
        return self.primer_nodo is None
        #return self.size == 0

    def agregar_final(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.esta_vacia():
            self.primer_nodo = nuevo
        else:
            actual = self.primer_nodo
            while actual.get_siguiente() is not None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo)
        self.size += 1

    def agregar_inicio(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.esta_vacia():
            self.primer_nodo = nuevo
        else:
            nuevo.set_siguiente(self.primer_nodo)
            self.primer_nodo = nuevo
        self.size += 1

    def imprimir(self):
        tmp = self.primer_nodo
        while tmp != None:
            print(tmp.get_dato())
            tmp = tmp.get_siguiente()

    def graficar(self, nombre_archivo):
        graph = Graph(nombre_archivo)
        tmp = self.primer_nodo
        while tmp != None:
            graph.add(tmp, tmp.get_siguiente())
            tmp = tmp.get_siguiente()
        graph.generar()

    def convertir_a_binario(self):
        tmp = self.primer_nodo
        while tmp != None:
            if(int(tmp.get_dato())>=1):
                tmp.set_dato(1)
            tmp = tmp.get_siguiente()
