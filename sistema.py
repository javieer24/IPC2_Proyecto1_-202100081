from abc import ABC, abstractmethod


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
        """
        Simula la señal a través del sistema.

        Args:
            senal: La señal a simular.

        Returns:
            La señal de salida del sistema.
        """
        pass

    # Métodos abstractos
    @abstractmethod
    def obtener_salida(self):
        """
        Obtiene la salida del sistema.

        Returns:
            La señal de salida del sistema.
        """
        pass

    # Métodos concretos
    def inicializar_sistema(self):
        # Aquí puedes implementar la lógica para inicializar el sistema
        pass

    def mostrar_datos(self):
        # Aquí puedes implementar la lógica para mostrar los datos del sistema
        pass    
    