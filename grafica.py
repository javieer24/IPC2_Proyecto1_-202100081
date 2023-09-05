import graphviz
class Grafica:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.dot = graphviz.Digraph('structs', filename=f'{self.nombre_archivo}.gv', node_attr={'shape': 'record', 'fontname': 'Helvetica'})
        self.dot.attr(rankdir='LR')  # Orientación horizontal (izquierda a derecha)

    def add(self, nodoInicio, nodoSiguiente):
        if nodoSiguiente is not None:
            self.dot.node(str(nodoInicio.getId()), str(nodoInicio.getDato()))
            self.dot.node(str(nodoSiguiente.getId()), str(nodoSiguiente.getDato()))
            self.dot.edge(str(nodoInicio.getId()), str(nodoSiguiente.getId()))

    def generar(self, formato_salida='png'):
        archivo_salida_path = f'img/{self.nombre_archivo}.{formato_salida}'
        self.dot.render(filename=archivo_salida_path, format=formato_salida, view=False)
        return archivo_salida_path



def generar_grafica(nombre_archivo):
    # Aquí puedes implementar la lógica para generar una gráfica utilizando Graphviz
    dot = graphviz.Graph()
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

def generar_grafica_desde_xml(nombre_archivo):
    # Aquí puedes implementar la lógica para generar una gráfica utilizando Graphviz
    dot = graphviz.Graph()
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