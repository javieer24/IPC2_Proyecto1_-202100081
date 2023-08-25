import graphviz

class Grafica:
    def generar_grafica(self, nombre, datos):
        dot = graphviz.Digraph()
        # Aquí se puede implementar la lógica para agregar nodos y aristas a la gráfica utilizando los datos
        dot.render(nombre + '.gv', view=True, format='png')

class Graph():
    def __init__(self):
        self.dot = graphviz.Digraph('structs', filename='structs.gv', node_attr={'shape': 'record', 'fontname':'Helvetica'})    

    def add(self, nodoInicio, nodoSiguiente):
        if(nodoSiguiente != None):
            self.dot.node(str(nodoInicio.getId()), str(nodoInicio.getDato()))
            self.dot.node(str(nodoSiguiente.getId()), str(nodoSiguiente.getDato()))
            self.dot.edge(str(nodoInicio.getId()), str(nodoSiguiente.getId()))

    def generar(self):
       self.dot.render(outfile='img/structs.png').replace('\\', '/')
       'img/structs.png'

def generar_grafica():
    # Aquí puedes implementar la lógica para generar una gráfica utilizando Graphviz
    dot = Digraph()
    dot.node('Prueba 1 reducida')
    dot.node('5')
    dot.node('7')
    dot.node('0')
    dot.node('6')
    dot.node('0_2')
    dot.node('9')
    dot.node('4')
    dot.edges([('Prueba 1 reducida', '5'), ('Prueba 1 reducida', '7'), ('Prueba 1 reducida', '0'), ('Prueba 1 reducida', '6'), ('Prueba 1 reducida', '0_2'), ('Prueba 1 reducida', '9'), ('Prueba 1 reducida', '4')])
    dot.edge('Prueba 1 reducida', '5', label='g=1(t-1.3)')
    dot.edge('Prueba 1 reducida', '7', label='g=2(t-2.5)')
    # Aquí puedes agregar más nodos y aristas a la gráfica
    dot.render('prueba.gv', view=True, format='png')
