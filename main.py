from turtle import dot
from graphviz import Digraph
from archivo import *
import xml.etree.ElementTree as ET 
from grafica import Grafica
import graphviz as gv
import os
from archivo import cargar_archivo, escribir_archivo_salida
from archivo import generar_grafica
# Agregar una variable para verificar si se ha cargado un archivo
archivo_xml_cargado = False
# Agregar una variable para verificar si se ha cargado un archivo
archivo_cargado = False
# Formatos de archivo de salida predeterminados compatibles
formatos_salida_compatibles = ["png", "svg"]
archivo_salida_formato = "png"  
archivo_cargado=True
# Formato de archivo de salida predeterminado

# Obtener la ruta raíz del proyecto
ruta_proyecto = os.getcwd()  # Esto obtiene la ruta del directorio de trabajo actual

nombre_grafica_generada = None

def inicializar_sistema():
    global datos_archivo_xml, ruta_proyecto, nombre_grafica_generada

    # Verificar si hay datos cargados y eliminarlos
    if datos_archivo_xml is not None:
        print("Eliminando datos cargados...")
        datos_archivo_xml = None

    # Eliminar archivo XML cargado si existe
    if os.path.exists(os.path.join(ruta_proyecto, "archivo.xml")):
        print("Eliminando archivo XML cargado...")
        os.remove(os.path.join(ruta_proyecto, "archivo.xml"))

    # Eliminar archivo PNG o SVG generado si existe
    if nombre_grafica_generada:
        nombre_archivo_generado = f"{nombre_grafica_generada}.png"  # o .svg
        if os.path.exists(os.path.join(ruta_proyecto, nombre_archivo_generado)):
            print(f"Eliminando archivo PNG o SVG generado: {nombre_archivo_generado}")
            os.remove(os.path.join(ruta_proyecto, nombre_archivo_generado))

    print("Sistema inicializado con éxito.")
   
    pass
  
def mostrar_datos_estudiante():
    # Aquí puedes implementar la lógica para mostrar los datos del estudiante
    print("Nombre del estudiante:", "Javier Andrés Monjes Solórzano")    
    print("Carné del estudiante:", "202100081")  
    print("Introducción a la Programación y Computación 2 Sección \"A\"")    
    print("Ingeniería en Ciencias y Sistemas")    
    print("4to Semestre")   
    pass

# Define una matriz de prueba
matriz = [
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 1, 0, 1]
]

# Define las matrices matriz_binaria y matriz_acceso antes de procesar el archivo
matriz_binaria = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]
matriz_acceso = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

def procesar_archivo():
    # Aquí puedes implementar la lógica para procesar el archivo cargado previamente
    print("Calculando la matriz binaria...")
    # Aquí puedes implementar la lógica para calcular la matriz binaria
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                matriz_binaria[i][j] = 1

    print("Realizando suma de tuplas...")
    # Aquí puedes implementar la lógica para realizar la suma de tuplas
    for i in range(len(matriz_binaria)):
        for j in range(len(matriz_binaria)):
            if i != j and matriz_binaria[i] == matriz_binaria[j]:
                for k in range(len(matriz[i])):
                    matriz_acceso[i][k] += matriz[j][k]
    pass

# Agregar una variable para verificar si se ha cargado un archivo XML
archivo_xml_cargado = False
# Agregar una variable para verificar si se ha cargado un archivo (podría estar relacionada con el problema)
archivo_cargado = False
# Formatos de archivo de salida predeterminados compatibles
formatos_salida_compatibles = ["png", "svg"]
archivo_salida_formato = "png"  # Formato de archivo de salida predeterminado

# Obtener la ruta raíz del proyecto
ruta_proyecto = os.getcwd()  # Esto obtiene la ruta del directorio de trabajo actual

def main():
    global archivo_xml_cargado, datos_archivo_xml

    while True:
        print("Menú principal:")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Inicializar sistema")
        print("7. Salida")

        opcion = input("Ingrese una opción: ")

        if opcion.isdigit():  # Verifica si la entrada es un número
            opcion = int(opcion)  # Convierte la entrada a un entero

            if 1 <= opcion <= 7:  # Verifica si la opción está en el rango válido
                if opcion == 1:
                    ruta = input("Ingrese la ruta del archivo: ")

                    confirmacion = input(f"¿Está seguro de que '{ruta}' es la ruta correcta? (S/N): ").strip().upper()

                    if confirmacion == 'S':
                        archivo_xml_cargado = cargar_archivo(ruta)
                        if archivo_xml_cargado:
                            print("Archivo cargado con éxito.")
                elif opcion == 2:
                    if not archivo_xml_cargado:
                        print("No se ha cargado un archivo. Por favor, cargue un archivo primero.")
                    else:
                        procesar_archivo()
                elif opcion == 3:
                    if archivo_cargado:
                        formato_salida = input("Elija el formato del archivo de salida (PNG o SVG): ").strip().lower()
                        escribir_archivo_salida(formato_salida)
                    else:
                        formato_salida = input("Elija el formato del archivo de salida (PNG o SVG)(escriba en minúsculas): ").strip().lower()
                        if formato_salida in ["png", "svg"]:
                            escribir_archivo_salida(formato_salida)
                        else:
                            print(f"El formato de salida '{formato_salida}' no es válido. Por favor, elija un formato válido.")
                    if not archivo_xml_cargado:
                        print("No se ha cargado un archivo. Por favor, cargue un archivo primero.")
                    
                elif opcion == 4:
                    mostrar_datos_estudiante()
            
                elif opcion == 5:
                    if archivo_xml_cargado:
                        formato_salida = input("Elija el formato del archivo de salida (PNG o SVG): ").strip().lower()
                        nombre_archivo = input("Ingrese el nombre del archivo de salida: ").strip()
                        generar_grafica(nombre_archivo, formato_salida)
                    else:
                        print("No se ha cargado un archivo. Por favor, cargue un archivo primero.")
                
                elif opcion == 6:
                    inicializar_sistema()  # Esta opción permite inicializar el sistema
                elif opcion == 7:
                    print("Saliendo del programa...")
                    break
            else:
                print("Opción no válida. Ingrese una opción entre 1 - 7.")
        else:
            print("Entrada no válida. Ingrese un número del menú (1-7).")

if __name__ == "__main__":
    archivo_xml_cargado = False
    datos_archivo_xml = None
    main()
