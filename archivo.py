import xml.etree.ElementTree as ET
from graphviz import Digraph
import os

# Agregar una variable para verificar si se ha cargado un archivo XML
archivo_xml_cargado = False

# Agregar la variable datos_archivo_xml aquí
datos_archivo_xml = None  # Esta variable almacenará los datos del archivo XML

# Formatos de archivo de salida predeterminados compatibles
formatos_salida_compatibles = ["png", "svg"]
archivo_salida_formato = "png"  # Formato de archivo de salida predeterminado

# Obtener la ruta raíz del proyecto
ruta_proyecto = os.getcwd()  # Esto obtiene la ruta del directorio de trabajo actual

# Modificar la opción 1 para cargar el archivo y realizar la conversión
# Modificar la opción 1 para cargar el archivo y realizar la conversión
def cargar_archivo(ruta):
    global datos_archivo_xml  # Indica que vamos a modificar la variable global
    try:
        ruta = os.path.join(ruta_proyecto, ruta)  # Obtener la ruta absoluta del archivo
        tree = ET.parse(ruta)
        root = tree.getroot()

        # Guardar los datos del archivo XML cargado en la variable global
        datos_archivo_xml = root  # Guardar el elemento root del XML

        # Mostrar mensaje de confirmación
        print(f"Archivo XML cargado desde: {ruta}")
        return root  # Devolver el elemento root del XML
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None  # En caso de error, devolver None


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
    
    
# Coloca el código que te proporcioné aquí
import xml.etree.ElementTree as ET

# Cargar el archivo XML de entrada
entrada_xml = "entrada.xml"
arbol = ET.parse(entrada_xml)
raiz = arbol.getroot()

# Crear un nuevo árbol para el formato de salida
salida_xml = ET.Element("senalesReducidas")

# Iterar a través de las señales en el XML de entrada
for senal in raiz.findall('senal'):

# Crear un nuevo archivo XML con el formato de salida
    salida_xml_tree = ET.ElementTree(salida_xml)
    salida_xml_tree.write("salida.xml", encoding="utf-8", xml_declaration=True)

print("Transformación completada. El archivo de salida 'salida.xml' ha sido generado.")

def obtener_datos_archivo_xml():
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


# Modificar la opción 3 para generar solo el archivo de salida y el nuevo XML
def escribir_archivo_salida(formato_grafica):
    global matriz_patrones_acceso, frecuencias_filas, grado_matrices, dimensiones_matrices

    # Verifica si se han calculado las matrices y las frecuencias
    if matriz_patrones_acceso is None or frecuencias_filas is None:
        print("No se han calculado las matrices de patrones de acceso o las frecuencias de las filas.")
        return

    # Comienza a construir el XML
    nueva_raiz = ET.Element("datos_proyecto")

    # Agrega información sobre las dimensiones de las matrices
    dimensiones_element = ET.SubElement(nueva_raiz, "dimensiones_matrices")
    for i, dimension in enumerate(dimensiones_matrices):
        dim_element = ET.SubElement(dimensiones_element, f"dimension_{i+1}")
        dim_element.text = str(dimension)

    # Agrega información sobre el grado de las matrices
    grado_element = ET.SubElement(nueva_raiz, "grado_matrices")
    grado_element.text = str(grado_matrices)

    # Agrega las matrices de patrones de acceso y sus frecuencias
    matrices_element = ET.SubElement(nueva_raiz, "matrices_patrones_acceso")
    for i, matriz in enumerate(matriz_patrones_acceso):
        matriz_element = ET.SubElement(matrices_element, f"matriz_{i+1}")
        
        # Agrega la matriz como una cadena de texto
        matriz_texto = ' '.join(map(str, matriz))
        matriz_element.text = matriz_texto
        
        # Agrega la frecuencia de la fila correspondiente
        frecuencia_element = ET.SubElement(matriz_element, "frecuencia")
        frecuencia_element.text = str(frecuencias_filas[i])

    # Genera el archivo XML
    archivo_salida = "Archivo_Salida.xml"
    ruta_proyecto = os.getcwd()  # Cambia la ruta si es necesario
    ruta_completa = os.path.join(ruta_proyecto, archivo_salida)

    try:
        # Escribe el XML en el archivo
        with open(ruta_completa, "wb") as xml_file:
            xml_file.write(ET.tostring(nueva_raiz))
        print(f"El archivo XML con los datos de patrones de acceso se ha guardado como '{archivo_salida}'.")

        # Guarda la gráfica en el formato especificado (PNG o SVG)
        if formato_grafica in ('png', 'svg'):
            nombre_grafica = input("Ingrese el nombre del archivo de gráfica de salida: ")
            generar_grafica(nombre_grafica, formato_grafica)
            print(f"La gráfica se ha guardado como '{nombre_grafica}' en formato {formato_grafica}.")
        else:
            print("Formato de gráfica no válido. No se ha guardado la gráfica.")

    except Exception as e:
        print(f"Error al escribir el archivo XML: {e}")

# Modificar la opción 5 para generar solo el archivo de salida y el nuevo XML
def generar_grafica(nombre_archivo, formato_salida):
    global datos_archivo_xml, ruta_proyecto

    if not datos_archivo_xml:
        print("No se han cargado datos del archivo XML. Por favor, cargue un archivo primero.")
        return

    # Obtener el nombre de la primera señal del archivo XML
    nombre_grafica = datos_archivo_xml[0].get('nombre')

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
