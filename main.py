from turtle import dot
from graphviz import Digraph
from archivo import *
import xml.etree.ElementTree as ET 
from grafica import Grafica
import graphviz as gv
import os
from grafica import generar_grafica
# Agregar una variable para verificar si se ha cargado un archivo
archivo_xml_cargado = False
# Agregar una variable para verificar si se ha cargado un archivo
archivo_cargado = False
# Formatos de archivo de salida predeterminados compatibles
formatos_salida_compatibles = ["png", "svg"]
archivo_salida_formato = "png"  # Formato de archivo de salida predeterminado

# Obtener la ruta raíz del proyecto
ruta_proyecto = os.getcwd()  # Esto obtiene la ruta del directorio de trabajo actual


def inicializar_sistema():
    # Aquí se puede implementar la lógica para inicializar el sistema
    pass
  
def mostrar_datos_estudiante():
    # Aquí puedes implementar la lógica para mostrar los datos del estudiante
    print("Nombre del estudiante:", "Javier Andrés Monjes Solórzano")    
    print("Carné del estudiante:", "202100081")  
    print("Introducción a la Programación y Computación 2 Sección \"A\"")    
    print("Ingeniería en Ciencias y Sistemas")    
    print("4to Semestre")   
    pass

# ...
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
    global archivo_xml_cargado

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

        if opcion == "1":
            ruta = input("Ingrese la ruta del archivo: ")

            confirmacion = input(f"¿Está seguro de que '{ruta}' es la ruta correcta? (S/N): ").strip().upper()

            if confirmacion == 'S':
                archivo_xml_cargado = cargar_archivo(ruta)
                if archivo_xml_cargado:
                    print("Archivo cargado con éxito.")

        elif opcion == "2":
            if not archivo_xml_cargado:
                print("No se ha cargado un archivo. Por favor, cargue un archivo primero.")
            else:
                procesar_archivo()

        elif opcion == "3":
            if not archivo_xml_cargado:
                print("No se ha cargado un archivo. Por favor, cargue un archivo primero.")
            else:
                formato_salida = input("Elija el formato del archivo de salida (PNG o SVG)(escriba en minusculas): ").strip().lower()
                if formato_salida in ["png", "svg"]:
                    escribir_archivo_salida(formato_salida)
                else:
                    print(f"El formato de salida '{formato_salida}' no es válido. Por favor, elija un formato válido.")

        elif opcion == "4":
            mostrar_datos_estudiante()

        elif opcion == "5":
            if archivo_xml_cargado:
                formato_salida = input("Elija el formato del archivo de salida (PNG o SVG): ").strip().lower()
                generar_grafica(formato_salida)  # Corregir el nombre de la función

        elif opcion == "6":
            inicializar_sistema()  # Esta opción permite inicializar el sistema

        elif opcion == "7":
            break

if __name__ == "__main__":
    archivo_xml_cargado = False
    datos_archivo_xml = None
    main()