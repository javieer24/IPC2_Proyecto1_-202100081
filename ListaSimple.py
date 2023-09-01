from nodo import Nodo
from grafica import Grafica

# Clase para representar listas simples
class ListaSimple:

    # Clase para representar listas simples

    id = 0

    # Comentario para explicar el propósito del atributo `nodoInicio`

    def __init__(self):
        # Comentario para explicar el propósito del constructor
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0

    # Comentario para explicar el propósito del método `getInicio()`

    def getInicio(self):
        # Comentario para explicar el propósito del método
        return self.nodoInicio

    # Comentario para explicar el propósito del método `estaVacia()`

    def estaVacia(self):
        # Comentario para explicar el propósito del método
        return self.nodoInicio == None

    # Comentario para explicar el propósito del método `agregarFinal()`

    def agregarFinal(self, dato):
        # Comentario para explicar el propósito del método
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            # Comentario para explicar el caso en el que la lista está vacía
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            # Comentario para explicar el caso en el que la lista no está vacía
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size += 1

    # Comentario para explicar el propósito del método `agregarInicio()`

    def agregarInicio(self, dato):
        # Comentario para explicar el propósito del método
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            # Comentario para explicar el caso en el que la lista está vacía
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            # Comentario para explicar el caso en el que la lista no está vacía
            nuevo.setSiguiente(self.nodoInicio)
            self.nodoInicio = nuevo
        self.size += 1

    # Comentario para explicar el propósito del método `agregarEnOrden()`

    def agregarEnOrden(self, dato):
        # Comentario para explicar el propósito del método
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            # Comentario para explicar el caso en el que la lista está vacía
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        elif dato < self.nodoInicio.getDato():
            # Comentario para explicar el caso en el que el dato es menor que el primer elemento de la lista
            nuevo.setSiguiente(self.nodoInicio)
            self.nodoInicio = nuevo
        elif dato > self.nodoFinal.getDato():
            # Comentario para explicar el caso en el que el dato es mayor que el último elemento de la lista
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        else:
            # Comentario para explicar el caso en el que el dato está entre los elementos de la lista
            tmp = self.nodoInicio
            while tmp.getSiguiente().getDato() < dato:
                tmp = tmp.getSiguiente()
            nuevo.setSiguiente(tmp.getSiguiente())
            tmp.setSiguiente(nuevo)
        self.size += 1

    # Comentario para explicar el propósito del método `eliminarInicio()`

    def eliminarInicio(self):
        if not self.estaVacia():
            if self.nodoInicio == self.nodoFinal:
                # Comentario para explicar el caso en el que la lista tiene un solo elemento
                self.nodoInicio = None
                self.nodoFinal = None
            else:
                # Comentario para explicar el caso en el que la lista no está vacía
                self.nodoInicio = self.nodoInicio.getSiguiente()
                self.nodoInicio.setAnterior(None)
        self
