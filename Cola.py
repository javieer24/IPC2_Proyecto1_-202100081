from ListaSimple import ListaSimple # Importar la clase ListaSimple del archivo ListaSimple.py  
class Cola(ListaSimple):

    def enconlar(self, elemento):
        ListaSimple.agregarInicio(self, elemento)

    def desencolar(self):
        ListaSimple.eliminarFinal(self)

    def graficar(self, nombre="cola"):
        ListaSimple.graficar(self, nombre, "LR")
