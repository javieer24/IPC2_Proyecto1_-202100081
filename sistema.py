from senal import Senal

# Clase para representar los sistemas
class Sistema(ABC):
    # Atributos
    nombre: str
    tipo: str

    # Constructor
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    # Métodos abstractos
    @abstractmethod
    def simular_senal(self, senal):
        pass

    # Métodos abstractos
    @abstractmethod
    def obtener_salida(self):
        pass

# Clase para representar el sistema de primer orden
class SistemaPrimerOrden(Sistema):
    # Atributos
    constante_de_tiempo: float
    ganancia: float

    # Constructor
    def __init__(self, nombre, tipo, constante_de_tiempo, ganancia):
        super().__init__(nombre, tipo)
        self.constante_de_tiempo = constante_de_tiempo
        self.ganancia = ganancia

    # Implementación del método simular_senal()
    def simular_senal(self, senal):
        # Aquí puedes implementar la lógica para simular la señal a través del sistema
        pass

    # Implementación del método obtener_salida()
    def obtener_salida(self):
        # Aquí puedes implementar la lógica para obtener la salida del sistema
        pass

# Clase para representar el sistema de segundo orden
class SistemaSegundoOrden(Sistema):
    # Atributos
    constante_de_tiempo_1: float
    constante_de_tiempo_2: float
    ganancia: float

    # Constructor
    def __init__(self, nombre, tipo, constante_de_tiempo_1, constante_de_tiempo_2, ganancia):
        super().__init__(nombre, tipo)
        self.constante_de_tiempo_1 = constante_de_tiempo_1
        self.constante_de_tiempo_2 = constante_de_tiempo_2
        self.ganancia = ganancia

    # Implementación del método simular_senal()
    def simular_senal(self, senal):
        # Aquí puedes implementar la lógica para simular la señal a través del sistema
        pass

    # Implementación del método obtener_salida()
    def obtener_salida(self):
        # Aquí puedes implementar la lógica para obtener la salida del sistema
        pass
