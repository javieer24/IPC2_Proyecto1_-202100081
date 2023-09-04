from ListaSimple import ListaSimple

class Pila(ListaSimple): #uso de herencia

    def push(self, dato):
        ListaSimple.agregar_inicio(self, dato)
    
    def imprimir(self):
        ListaSimple.imprimir(self)

    def graficar(self, nombreArchivo):
        ListaSimple.graficar(self, nombreArchivo)

    def convertirABinario(self):
        ListaSimple.convertir_a_binario(self)

    def pop(self):
        if self.esta_vacia():
            print("La pila está vacía")
        else:
            tmp = self.primer_nodo
            self.primer_nodo = self.primer_nodo.get_siguiente()
            self.size -= 1
            return tmp.get_dato()
