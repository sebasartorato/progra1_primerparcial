'''
Aquí se encuentran las funciones de archivos (leer y crear) para el Json y el CSV.
'''

PATH = r'C:\Users\sebas\Documents\UTN\Lab Progra - 2024\1er_Parcial_2024\Proyectos.csv' #Ruta para CSV
PATH_JSON = r"C:\Users\sebas\Documents\UTN\Lab Progra - 2024\1er_Parcial_2024\ProyectosFinalizados.json" #Ruta para JSON

import json

def leer_csv () -> list:
    '''
    Funcion que lee el csv importado desde una ruta especifica (PATH -> constante).
    Crea la lista con los diccionarios.
    Verifica que no haya un error al intentar importar con un try/except manejando excepciones.
    Retorna la lista de diccionarios creada.
    '''

    #Intento abrir el archivo y si lo hace, creo la lista de diccionarios.
    try:
        with open(PATH, 'r', encoding='utf-8') as file:
            encabezado = file.readline()
            datos = file.readlines()  # Leer todas las líneas excepto la primera

        lista_encabezados = encabezado.strip().split(",")

        lista_diccionarios = []

        for linea in datos:
            valores = linea.strip().split(",")

            diccionario_fila = {}

            for i, valor in enumerate(valores):
                diccionario_fila.update({lista_encabezados[i]: valor})

            lista_diccionarios.append(diccionario_fila)

        return lista_diccionarios

    #Manejo errores dependiendo de cual sea, si no lo encuentra la ruta o si hay una excepción
    except FileNotFoundError: 
        print("El archivo no se pudo encontrar o abrir.")
        return []
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        return []

def sobrescribir_csv (lista_diccionarios: list) -> bool:
    '''
    Sobrescribe la lista de diccionarios en el archivo CSV. Se fija que la lista no esté vacía
    para luego concatenar la información y guardarla allí al finalizar el menú.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    Retorno: bool: True si la escritura en el archivo CSV fue exitosa, 
    False en caso contrario.
    '''
    retorno = False
    
    try:
        if lista_diccionarios:
            encabezado = "id,Nombre del Proyecto,Descripción,Fecha de inicio,Fecha de Fin,Presupuesto,Estado\n"
            informacion = ""

            for proyecto in lista_diccionarios:
                informacion += proyecto["id"] + "," + proyecto["Nombre del Proyecto"] + "," + proyecto["Descripción"] + "," + str(proyecto["Fecha de inicio"]) + ","+ str(proyecto["Fecha de Fin"])+ "," + str(proyecto["Presupuesto"]) + "," + proyecto["Estado"] +"\n"
            
            informacion_total = encabezado + informacion
            #Extraigo encabezados abriendo el archivo
            with open(PATH, "w+", encoding = "utf-8") as file:
                file.write(informacion_total)
            retorno = True
        else:
            print("La lista está vacía...")
    except FileNotFoundError: 
        print("El archivo no se pudo encontrar o abrir.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

    return retorno

def crear_json_finalizados (lista_diccionarios: str):
    '''
    Funcion que se encarga de crear un JSON con los diccionarios cuyo estado
    sea "Finalizado". Maneja excepciones con un try/except por si no se pudo
    crear el archivo
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    No retorna nada.
    '''
    
    lista_finalizados = []

    for diccionario in lista_diccionarios:
        if diccionario["Estado"] == "Finalizado":
            lista_finalizados.append(diccionario)
    
    try:
        with open(PATH_JSON, "w", encoding='utf-8') as archivo:
            json.dump(lista_finalizados, archivo, indent=4, ensure_ascii=False)
        print("JSON creado con proyectos Finalizados.")
    except FileNotFoundError: 
        print("El archivo no se pudo encontrar o abrir.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")