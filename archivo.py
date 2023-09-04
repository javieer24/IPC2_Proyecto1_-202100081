import xml.etree.ElementTree as ET
from graphviz import Digraph
import os
# Agregar una variable para verificar si se ha cargado un archivo XML
archivo_xml_cargado = False
# Agregar una variable para verificar si se ha cargado un archivo (podría estar relacionada con el problema)
archivo_cargado = False
# Formatos de archivo de salida predeterminados compatibles
formatos_salida_compatibles = ["png", "svg"]
archivo_salida_formato = "png"  # Formato de archivo de salida predeterminado

# Obtener la ruta raíz del proyecto
ruta_proyecto = os.getcwd()  # Esto obtiene la ruta del directorio de trabajo actual

# Modificar la opción 1 para cargar el archivo y realizar la conversión
def cargar_archivo(ruta):
    global datos_archivo_xml, archivo_xml_cargado  # Acceder a las variables globales

    try:
        tree = ET.parse(ruta)
        root = tree.getroot()

        # Guardar los datos del archivo XML cargado en la variable global
        datos_archivo_xml = root

        # Establecer archivo_xml_cargado en True después de cargar el archivo con éxito
        archivo_xml_cargado = True

        # Mostrar mensaje de confirmación
        print(f"Archivo XML cargado desde: {ruta}")
        return True  # Devolver True si la carga fue exitosa
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return False  # Devolver False en caso de error

def obtener_datos_archivo_xml(ruta):
    global datos_archivo_xml

    try:
        if datos_archivo_xml is not None:
            datos_senales = []

            for senal in datos_archivo_xml.findall('senal'):
                nombre = senal.get('nombre')
                datos = []

                for dato in senal.findall('dato'):
                    t = dato.get('t')
                    A = dato.get('A')
                    valor = dato.text if dato.text else "0"  # Si no hay valor, se usa "0"
                    datos.append((t, A, valor))

                datos_senales.append({'nombre': nombre, 'datos': datos})

            return datos_senales

        else:
            print("No se ha cargado un archivo XML. Por favor, cargue un archivo primero.")
            return []

    except Exception as e:
        print(f"Error al obtener datos del archivo XML: {e}")
        return []

def guardar_datos(datos, nombre_archivo):
    try:
        # Guardar los datos en el archivo
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(datos)

        print(f"Los datos se han guardado en '{nombre_archivo}'")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
    pass

def procesar_archivo():
    global archivo_xml_cargado

    if not archivo_xml_cargado:
        print("No se ha cargado un archivo. Por favor, cargue un archivo primero.")
        return

    # Aquí puedes implementar la lógica para procesar el archivo cargado previamente
    print("Calculando la matriz binaria...")
    # Aquí puedes implementar la lógica para calcular la matriz binaria
    print("Realizando suma de tuplas...")
    # Aquí puedes implementar la lógica para realizar la suma de tuplas

import os
# Obtener la ruta raíz del proyecto
ruta_proyecto = os.getcwd()  # Esto obtiene la ruta del directorio de trabajo actual

# ...

# Modificar la opción 3 para generar solo el archivo de salida y el nuevo XML
def escribir_archivo_salida(formato_salida):
    global archivo_cargado, ruta_proyecto, datos_archivo_xml  # Acceder a las variables globales

    if not archivo_xml_cargado:
        print("No se ha cargado un archivo XML. Por favor, cargue un archivo primero.")
        return

    # Verificar si el formato de salida es válido (PNG o SVG)
    if formato_salida not in ('png', 'svg'):
        print("Formato no válido. Se generará el archivo en formato SVG por defecto.")
        formato_salida = 'svg'

    # Obtener el nombre del archivo cargado desde los datos del XML
    if datos_archivo_xml is not None:
        nombre_grafica = datos_archivo_xml.find('nombre').text
    else:
        print("No se ha cargado un archivo XML. Por favor, cargue un archivo primero.")
        return

    # Generar la gráfica y guardarla en el formato especificado
    generar_grafica(nombre_grafica, formato_salida)

    print(f"La gráfica se ha guardado como '{nombre_grafica}.{formato_salida}'.")

    # Crear el nuevo archivo XML con la información de la gráfica
    nueva_raiz = ET.Element("nueva_raiz")
    nueva_senal = ET.SubElement(nueva_raiz, "nueva_senal", nombre=nombre_grafica)
    nueva_dato = ET.SubElement(nueva_senal, "dato", t="1", A="1")

    nuevo_archivo_xml = os.path.join(ruta_proyecto, f"{nombre_grafica}.xml")
    with open(nuevo_archivo_xml, "wb") as xml_file:
        xml_file.write(ET.tostring(nueva_raiz))

    print(f"El archivo XML con la información de la gráfica se ha guardado como '{nuevo_archivo_xml}'.")
    
    
# Modificar la opción 5 para generar la gráfica en el archivo de salida
def generar_grafica(nombre_archivo, formato_salida):
    global datos_archivo_xml, ruta_proyecto

    if not datos_archivo_xml:
        print("No se han cargado datos del archivo XML. Por favor, cargue un archivo primero.")
        return

    # Obtener el nombre de la gráfica a partir de los datos cargados
    nombre_grafica = datos_archivo_xml.find('nombre').text

    # Generar el nombre del archivo de salida con "v" al principio y el formato
    nombre_archivo_salida = f"v{nombre_grafica}.{formato_salida}"

    # Confirmar con el usuario si desea guardar la gráfica en el formato especificado
    confirmacion = input(f"¿Desea guardar la gráfica como '{nombre_archivo_salida}'? (S/N): ").strip().lower()

    if confirmacion == "s":
        dot_graph = Digraph(format=formato_salida)
        dot_graph.node(nombre_grafica)

        datos = obtener_datos_archivo_xml()

        for dato in datos:
            nodo_nombre = f"Nodo {dato['nombre']}"
            dot_graph.node(nodo_nombre)
            dot_graph.edge(nombre_grafica, nodo_nombre, label=f'g={dato["datos"][0][2]}(t-{dato["datos"][0][0]})')

        archivo_salida_path = os.path.join(ruta_proyecto, nombre_archivo_salida)
        dot_graph.render(archivo_salida_path, view=False)

        print(f"La gráfica se ha guardado como '{nombre_archivo_salida}'.")

        nueva_raiz = ET.Element("nueva_raiz")
        nueva_senal = ET.SubElement(nueva_raiz, "nueva_senal", nombre=nombre_grafica)
        nueva_dato = ET.SubElement(nueva_senal, "dato", t="1", A="1")

        nuevo_archivo_xml = os.path.join(ruta_proyecto, f"{nombre_grafica}.xml")
        with open(nuevo_archivo_xml, "wb") as xml_file:
            xml_file.write(ET.tostring(nueva_raiz))

        print(f"El archivo XML con la información de la gráfica se ha guardado como '{nuevo_archivo_xml}'.")
    else:
        print("La gráfica no se ha guardado.")
