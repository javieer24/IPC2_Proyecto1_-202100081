class Nodo:
    """
    Esta clase representa un nodo en una lista enlazada.
    Atributos:
        nombre: El nombre del nodo.
        siguiente: Una referencia al siguiente nodo en la lista.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente
