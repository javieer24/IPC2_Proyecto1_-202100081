from enum import Enum


class TipoNodo(Enum):
    """
    Esta clase representa los diferentes tipos de nodos que puede haber en una lista enlazada.
    """

    NODO_VACIO = 0
    NODO_SEÑAL = 1
    NODO_PUNTO = 2


class Nodo:

    """
    Esta clase representa un nodo en una lista enlazada.
    Atributos:
        tipo: El tipo de nodo.
        nombre: El nombre del nodo.
        valor: El valor del nodo.
        siguiente: Una referencia al siguiente nodo en la lista.
    """

    def __init__(self, tipo, nombre, valor):
        self.tipo = tipo
        self.nombre = nombre
        self.valor = valor
        self.siguiente = None

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente


