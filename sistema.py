from abc import ABC, abstractmethod


class Sistema(ABC):

    # Atributos
    nombre: str
    tipo: str
    archivo_xml_cargado: bool
    datos_archivo_xml: None
    formato_salida: str
    archivo_salida_generado: bool
    archivos_xml_cargados: list  # Lista para almacenar datos de XML cargados

    # Constructor
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.reiniciar_sistema()  # Llamar al método de reinicio en el constructor

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

    def reiniciar_sistema(self):
        # Este método reinicia el sistema y borra todos los datos
        # Puedes agregar aquí la lógica para reiniciar las variables y datos relevantes

        # Restablecer las variables relacionadas con archivos XML
        self.archivo_xml_cargado = False
        self.datos_archivo_xml = None
        self.archivos_xml_cargados = []  # Restablecer la lista de archivos XML cargados

        # Restablecer las variables relacionadas con archivos de salida
        self.formato_salida = "png"  # Formato de archivo de salida predeterminado
        self.archivo_salida_generado = False
