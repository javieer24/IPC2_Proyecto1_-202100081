from nodo import Nodo

class Lista:
    """
    Esta clase representa una lista enlazada.
    Atributos:
        cabeza: Una referencia a la cabeza de la lista.
    Métodos:
        insertar(nombre): Inserta un nuevo nodo con el nombre dado al final de la lista.
        buscar(nombre): Busca un nodo con el nombre dado en la lista y devuelve Verdadero si se encuentra, Falso en caso contrario.
        generar_reporte_grafico(): Genera un informe gráfico utilizando Graphviz (no implementado).
    """
    def __init__(self):
        self.cabeza = None

    def insertar(self, nombre):
        nuevo_nodo = Nodo(nombre)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar(self, nombre):
        actual = self.cabeza
        while actual is not None:
            if actual.nombre == nombre:
                return True
            actual = actual.siguiente
        return False

    def generar_reporte_grafico(self):
        # Aquí puedes implementar la lógica para generar un informe gráfico utilizando Graphviz
        pass
