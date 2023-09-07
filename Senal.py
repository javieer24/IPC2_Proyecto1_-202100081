from ListaSimple import ListaSimple
from Tiempo import Tiempo
from abc import ABC, abstractmethod
# Clase abstracta para representar las señales
class Senal(ABC):
    # Atributos
    nombre: str
    tiempoMaximo: float
    amplitudMaxima: float

    # Constructor
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima):
        self.nombre = nombre
        self.tiempoMaximo = tiempoMaximo
        self.amplitudMaxima = amplitudMaxima

    # Métodos abstractos
    @abstractmethod
    def obtenerAmplitud(self, tiempo):
        pass

    @abstractmethod
    def obtenerFrecuencia(self):
        pass

    @abstractmethod
    def obtenerTiempo(self):
        pass

# Clase para representar las señales de tipo sinusoidal
class SenalSinusoidal(Senal):
    # Atributo
    frecuencia: float

    # Constructor
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima, frecuencia):
        super().__init__(nombre, tiempoMaximo, amplitudMaxima)
        self.frecuencia = frecuencia

    # Implementación de los métodos abstractos
    def obtenerAmplitud(self, tiempo):
        return self.amplitudMaxima

    def obtenerFrecuencia(self):
        return self.frecuencia

    def obtenerTiempo(self):
        return self.tiempoMaximo

# Clase para representar las señales de tipo cuadrada
class SenalCuadrada(Senal):
    # Atributo
    periodo: float

    # Constructor
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima, periodo):
        super().__init__(nombre, tiempoMaximo, amplitudMaxima)
        self.periodo = periodo

    # Implementación de los métodos abstractos
    def obtenerAmplitud(self, tiempo):
        return self.amplitudMaxima

    def obtenerFrecuencia(self):
        return 1 / self.periodo

    def obtenerTiempo(self):
        return self.tiempoMaximo

# Clase para representar las señales de tipo triangular
class SenalTriangular(Senal):
    # Atributo
    periodo: float

    # Constructor
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima, periodo):
        super().__init__(nombre, tiempoMaximo, amplitudMaxima)
        self.periodo = periodo

    # Implementación de los métodos abstractos
    def obtenerAmplitud(self, tiempo):
        return self.amplitudMaxima * (2 * tiempo / self.periodo)

    def obtenerFrecuencia(self):
        return 1 / self.periodo

    def obtenerTiempo(self):
        return self.tiempoMaximo
