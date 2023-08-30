# Archivos de importación
from abc import ABC, abstractmethod
from Senal import Senal
from grafica import Grafica
from archivo import Archivo
from LecturaXML import LecturaXML

# Clases
class Reporte(ABC):
    @abstractmethod
    def generar_reporte(self):
        pass

class ReporteGrafico(Reporte):
    def generar_reporte(self):
        # Implementación del reporte gráfico utilizando Graphviz
        pass

class ReporteTabla(Reporte):
    def generar_reporte(self):
        # Implementación del reporte en forma de tabla
        pass