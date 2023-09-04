import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from  Senal import Senal
from Pila import Pila
from Cola import Cola
import copy

class LecturaXML():
    def __init__(self, path):
        self.raiz = ET.parse(path).getroot()
        self.pila = Pila()
        self.lista = ListaSimple()
        self.cola = Cola()

    def getSenal(self):
        listSenales = ListaSimple()
        for senal in self.raiz.findall('senal'):
            nombreSenal = senal.get('nombre')
            tiempoMaximo = senal.get('t')
            amplitudMaxima = senal.get('A')
            tmpSenal = Senal(nombreSenal, tiempoMaximo, amplitudMaxima)
            listSenales.agregar(tmpSenal)

        print("_____Lista de senales_____")
        for senal in listSenales:
            print(senal.getNombre())

    def getDatos(self):
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                self.pila.push(int(dato.text))
                self.lista.agregarEnOrden(int(dato.text))
                self.cola.encolar(int(dato.text))

        pilaBinaria = copy.deepcopy(self.pila)
        pilaBinaria.convertirABinario()
        pilaBinaria.graficar('pilaBinaria')
        self.pila.graficar('pila')
        self.lista.graficar('lista')
        self.cola.graficar('cola')
        self.cola.desencolar()
        self.cola.graficar('cola2')
        self.cola.desencolar()
        self.cola.graficar('cola3')


objLectura = LecturaXML('entrada2.xml')
#objLectura.getSenal()
objLectura.getDatos()
