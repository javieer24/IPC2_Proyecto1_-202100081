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
