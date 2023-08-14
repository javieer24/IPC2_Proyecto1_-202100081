import xml.etree.ElementTree as ET
from tkinter import *


# Menú
def cargar_archivo():
    # Aquí puedes implementar la lógica para cargar un archivo
    pass

def procesar_archivo():
    # Aquí puedes implementar la lógica para procesar un archivo
    pass

def escribir_archivo_salida():
    # Aquí puedes implementar la lógica para escribir un archivo de salida
    pass

def mostrar_datos_estudiante():
    # Aquí puedes implementar la lógica para mostrar los datos del estudiante
    pass

def generar_grafica():
    # Aquí puedes implementar la lógica para generar una gráfica
    pass

def inicializar_sistema():
    # Aquí puedes implementar la lógica para inicializar el sistema
    pass

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
        cargar_archivo()
    elif opcion == "2":
        procesar_archivo()
    elif opcion == "3":
        escribir_archivo_salida()
    elif opcion == "4":
        mostrar_datos_estudiante()
    elif opcion == "5":
        generar_grafica()
    elif opcion == "6":
        inicializar_sistema()
    elif opcion == "7":
        break
    

