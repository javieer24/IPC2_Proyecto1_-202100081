from ListaSimple import ListaSimple
from Amplitud import Amplitud
from sistema import Sistema

# Clase para representar las amplitudes
class Tiempo:
    # Atributos
    tiempo: float
    amplitud: float

    # Constructor
    def __init__(self, tiempo, amplitud):
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.listaAmplitudes = ListaSimple()
        self.llenarListadoAmplitudes()

    # Métodos

    def getTiempo(self):
        return self.tiempo

    def getAmplitud(self):
        return self.amplitud

    def llenarListadoAmplitudes(self):
        """
        Llena el listado de amplitudes para el tiempo especificado.

        Args:
            None

        Returns:
            None
        """
        for i in range(1, int(self.amplitud) + 1):
            amplitud = Amplitud(i)
            self.listaAmplitudes.agregarFinal(amplitud)

    def imprimir(self):
        print("_____Amplitudes para tiempo:", self.tiempo, "_____")
        for amplitud in self.listaAmplitudes:
            print(amplitud.getAmplitud())

# Función para graficar una lista de amplitudes
def graficar(listaAmplitudes):
    import matplotlib.pyplot as plt

    plt.plot([amplitud.getAmplitud() for amplitud in listaAmplitudes], label="Amplitud")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.show()

# Programa principal
if __name__ == "__main__":
    # Crear una lista de amplitudes
    listaAmplitudes = []
    for i in range(1, 9):
        amplitud = Amplitud(i)
        listaAmplitudes.append(amplitud)

    # Crear un tiempo
    tiempo = Tiempo(1, 8)

    # Agregar las amplitudes al tiempo
    for amplitud in listaAmplitudes:
        tiempo.listaAmplitudes.agregarFinal(amplitud)

    # Imprimir el tiempo
    tiempo.imprimir()

    # Graficar el tiempo
    graficar(tiempo.listaAmplitudes)

# Función para simular un sistema de control
def simularSistema(sistema, senal):
    salida = sistema.simular_senal(senal)
    return salida

# Programa principal
if __name__ == "__main__":
    # Crear un sistema de primer orden
    sistema = SistemaPrimerOrden("Sistema 1", "Primer orden", 10, 2)

    # Crear una señal
    senal = Senal(1, 10, 1)

    # Simular el sistema
    salida = simularSistema(sistema, senal)

    # Imprimir la salida del sistema
    print("Salida del sistema:", salida)
