'''
Funciones principales del proyecto para cada opción
'''

BAJA_CORRECTA = 1
BAJA_CANCELADA = 2
BAJA_ERRONEA = 3

RETOMAR_CORRECTO = 1
RETOMAR_CANCELADO = 2
RETOMAR_ERRONEO = 3

PATH = r"C:\Users\sebas\Documents\UTN\Lab Progra - 2024\1er_Parcial_2024\Proyectos.csv" #Ruta para CSV
PATH_JSON = r"C:\Users\sebas\Documents\UTN\Lab Progra - 2024\1er_Parcial_2024\ProyectosFinalizados.json" #Ruta para JSON

import os

from validations import *
from archive_functions import *
from datetime import datetime

#Punto EXTRA
def contar_dicts_finalizados(lista_diccionarios)-> int:
    '''
    Funcion que cuenta la cantidad de proyectos finalizados actualmente.
    Recibe la lista de diccionarios.
    Devuelve la cantidad de diccionarios finalizados.
    '''
    contador = 0
    
    for diccionario in lista_diccionarios:
        if diccionario["Estado"] == "Finalizado":
            contador+=1
            
    return contador 

def imprimir_finalizados_menor (lista_finalizados: list) -> bool:
    '''
    Funcion que se encarga de imprimir el top 3 de proyectos finalizados con menor presupuesto.
    Recibe la lista de proyectos finalizados.
    Retorna un booleano indicando si tuvo exito la impresion o no.
    '''
    retorno = False

    if lista_finalizados:
        print("Top 3 de los proyectos finalizados con menor presupuesto:\n")
        for proyecto in range(3):
            print(f"Nombre: {lista_finalizados[proyecto]["Nombre del Proyecto"]} - Presupuesto: $ {lista_finalizados[proyecto]["Presupuesto"]}")

        retorno = True
    
    return retorno
        
def selection_sort_finalizados_menor (lista_finalizados: list) -> bool:
    '''
    Funcion que mediante el metodo selection sort ordena la lista de menor a mayor
    segun los presupuestos.
    Recibe la lista de diccionarios con estado "Finalizado".
    Retorna un booleano indicando si tuvo exito el orden o no.
    '''
    retorno = False

    if lista_finalizados:
        for i in range(0, len(lista_finalizados)-1):
                menor = i
                for j in range(i+1, len(lista_finalizados)):
                    try:
                        valor_j = int(lista_finalizados[j]["Presupuesto"])
                        valor_menor = int(lista_finalizados[menor]["Presupuesto"])
                        if valor_j < valor_menor:
                            menor = j
                    except ValueError:
                            print("Error de formato... ")
                            continue     
                    
                lista_finalizados[i], lista_finalizados[menor] = lista_finalizados[menor], lista_finalizados[i]                

        retorno = True
    
    return retorno

def listar_finalizados_menor_prep (lista_diccionarios: list) -> bool:
    '''
    Funcion que se encarga de listar en una nueva lista los diccionarios finalizados 
    y luego ordenarlos e imprimirlos.
    Recibe la lista de diccionarios.
    Retorna un booleano indicando si se pudo ordenar e imprimir la lista.

    '''
    retorno = False

    lista_finalizados = []

    if lista_diccionarios:
        for diccionario in lista_diccionarios:
            if diccionario["Estado"] == "Finalizado":
                lista_finalizados.append(diccionario)
        
        if selection_sort_finalizados_menor (lista_finalizados):
            if imprimir_finalizados_menor (lista_finalizados):
                retorno = True
        else:
            print("No se pudo ordenar.")

    else:
        print("No se pudo calcular el top 3 de proyectos de menores presupuestos.")

    return retorno

#Punto S
def selection_sort_activos_otoño(lista_otoño: list) -> bool:
    '''Funcion que mediante el metodo selection sort ordena la lista de mayor a menor
    segun los presupuestos.
    Recibe la lista de diccionarios con estado "Finalizado".
    Retorna un booleano indicando si tuvo exito el orden o no.
    '''
    retorno = False

    if lista_otoño:
        for i in range(0, len(lista_otoño)-1):
                menor = i
                for j in range(i+1, len(lista_otoño)):
                    try:
                        valor_j = int(lista_otoño[j]["Presupuesto"])
                        valor_menor = int(lista_otoño[menor]["Presupuesto"])
                        if valor_j > valor_menor:
                            menor = j
                    except ValueError:
                            print("Error de formato... ")
                            continue     
                    
                lista_otoño[i], lista_otoño[menor] = lista_otoño[menor], lista_otoño[i]                

        retorno = True
    
    return retorno

def imprimir_proyectos_activos_otoño (lista_otoño: list)-> bool:
    '''
    Funcion que se encarga de imprimir la cantidad de proyectos activos arrancados durante otoño.
    Recibe la lista de diccionarios cuya fecha de inicializacion fue en otoño.
    Retorna un booleano indicando el exito o no de la funcion.
    '''
    retorno = False
    if lista_otoño:
        print("Lista con los proyectos activos en otoño de mayor presupuesto:\n")
        for proyecto in lista_otoño:
            print(f"Nombre: {proyecto["Nombre del Proyecto"]} - Fecha Inicio: {proyecto["Fecha de inicio"]} - Presupuesto: $ {proyecto["Presupuesto"]}")
        
        retorno = True
    
    return retorno

def calcular_proyectos_activos_otoño (lista_diccionarios: list)-> bool:
    '''
    Funcion que calcula la cantidad de proyectos activos en otoño y luego los imprime 
    mientras que no haya errores (o la lista esté vacía).
    Recibe la lista de diccionarios.
    Retorna un booleano indicando el exito o no de la funcion.
    '''
    retorno = False
    lista_otoño = []
    fecha_inicio_otoño = datetime.strptime("20-03", "%d-%m")
    fecha_fin_otoño = datetime.strptime("20-06", "%d-%m")

    if lista_diccionarios:
        for diccionario in lista_diccionarios:
            if diccionario["Estado"] == "Activo":
                fecha_inicio = datetime.strptime(diccionario["Fecha de inicio"], "%d-%m-%Y")
                fecha_inicio_sin_año = fecha_inicio.replace(year=1900) #Seteo año random

                if fecha_inicio_sin_año >= fecha_inicio_otoño and fecha_inicio_sin_año <= fecha_fin_otoño:
                    lista_otoño.append(diccionario)

        if selection_sort_activos_otoño(lista_otoño):
            if imprimir_proyectos_activos_otoño(lista_otoño):
                retorno = True
    else:
        print("No se pudo calcular los proyectos activos en otoño")

    return retorno

# Punto S

def imprimir_dict_orden (lista_diccionarios: list, opcion_orden: int, orden: str, llave)->bool:
    #Imprimo los nombres de los proyectos según si es por orden de nombre o fecha fin / presupuesto.
    #Recibe la lista de diccionarios, la opcion de orden, el orden (ascendente o descendente) y la llave del diccionario.
    #Retorna un booleano que verifica el exito o no de la funcion.

    print(f"Lista ordenada en forma {orden} por {llave}: ")

    if lista_diccionarios:
        for diccionario in lista_diccionarios:
            if opcion_orden == 1:
                print(f"{diccionario[llave]}")
                retorno = True
            else:
                print(f"{diccionario["Nombre del Proyecto"]} | {llave}: {diccionario[llave]}")
                retorno = True
    else:
        print("Lista vacia")
    
    return retorno

def ordenar_selection_sort(lista_diccionarios: list) -> bool:
    '''
    Funcion que ordena mediante el selection sort la lista de forma ascendente o descendente.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    Retorna un booleano que verifica el exito o no de la funcion.
    '''
    
    #Primero pido opciones de tipo y forma y las valido
    retorno = False
    menu_orden = '''- Seleccione tipo de orden:
              1- Nombre
              2- Presupuesto
              3- Fecha Inicio
              Su opcion: '''

    menu_forma = '''- Seleccione la forma:
                1- Ascendente
                2- Descendente
                Su opcion: '''
    
    opcion_orden = ingresar_entero(menu_orden, "Error, ingrese opciones validas", 1, 3)
    opcion_forma = ingresar_entero(menu_forma, "Error, ingrese opciones validas", 1, 2)

    #Defino como será la llave y el orden
    if opcion_orden == 1:
        llave = "Nombre del Proyecto"
    elif opcion_orden == 2:
        llave = "Presupuesto"
    else:
        llave = "Fecha de inicio"
    
    if opcion_forma == 1:
        orden = "ascendente"
    else:
        orden = "descendente"

    if lista_diccionarios:
    #Ordeno segun orden y tipo (si es por nombre, presupuesto o fecha)
        if orden == "ascendente":
            for i in range(len(lista_diccionarios) - 1):
                menor = i
                for j in range(i + 1, len(lista_diccionarios)):
                    if opcion_orden == 3:
                        try:
                            fecha_j = datetime.strptime(lista_diccionarios[j][llave], "%d-%m-%Y")
                            fecha_menor = datetime.strptime(lista_diccionarios[menor][llave], "%d-%m-%Y")
                            if fecha_j < fecha_menor:
                                menor = j
                        except ValueError:
                            print("Error de formato... ")
                            continue
                    elif opcion_orden == 2:
                        try:
                            valor_j = int(lista_diccionarios[j][llave])
                            valor_menor = int(lista_diccionarios[menor][llave])
                            if valor_j < valor_menor:
                                menor = j
                        except ValueError:
                            print("Error de formato... ")
                            continue
                    else:
                        if lista_diccionarios[j][llave] < lista_diccionarios [menor][llave]:
                            menor = j

                lista_diccionarios[i], lista_diccionarios[menor] = lista_diccionarios[menor], lista_diccionarios[i]

        else:
            for i in range (0, len(lista_diccionarios) -1):
                mayor = i
                for j in range (i+1, len(lista_diccionarios)):
                    if opcion_orden == 3:
                        try:
                            fecha_j = datetime.strptime(lista_diccionarios[j][llave], "%d-%m-%Y")
                            fecha_mayor = datetime.strptime(lista_diccionarios [mayor][llave], "%d-%m-%Y")
                            if fecha_j > fecha_mayor:
                                mayor = j
                        except ValueError:
                            print("Error de formato... ")
                            continue
                    elif opcion_orden == 2:
                        try:
                            valor_j = int(lista_diccionarios[j][llave])
                            valor_mayor = int(lista_diccionarios [mayor][llave])
                            if valor_j > valor_mayor:
                                mayor = j
                        except ValueError:
                            print("Error de formato... ")
                            continue                
                    else:
                        if lista_diccionarios[j][llave] > lista_diccionarios [mayor][llave]:
                            mayor = j

                lista_diccionarios[mayor], lista_diccionarios[i] = lista_diccionarios[i], lista_diccionarios[mayor]

        if imprimir_dict_orden (lista_diccionarios, opcion_orden, orden, llave):
            retorno = True
    else:
        print("La lista está vacía...")

    return retorno

def mostrar_todos(lista_diccionarios: list) -> bool:
    '''
    Funcion que se encarga de mostrar la lista de diccionarios verificando que no esté vacía primero.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    Retorna un booleano que verifica el exito o no de la funcion.
    '''
    
    retorno = False
    if lista_diccionarios:
        informacion = "| "
        encabezados = ["id","Nombre del Proyecto", "Descripción", "Presupuesto", "Fecha de Inicio", "Fecha de Fin", "Estado"]
        encabezados_join = " \t | \t ".join(encabezados)
        print("-" *180)
        print(f"| {encabezados_join} |")
        print("-" *180)

        for diccionario in lista_diccionarios:
            for clave in diccionario:
                if int(diccionario["id"]) != 1:
                    informacion += "| " + str(diccionario[clave]) + " "
                else:
                    informacion += str(diccionario[clave]) + " | "
            informacion = informacion.rstrip(" |") 
            informacion += " |\n"
        
        print(informacion)
        print("-"*180)
        retorno = True
    else:
        print("Lista vacía.")
    
    return retorno

def buscar_proyecto_nombre (lista_diccionarios: list, diccionario_a_buscar: dict) -> bool:
    '''
    Funcion que se encarga de buscar el proyecto por nombre ingresado por el usuario.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios
                Recibe un diccionario vacío que luego será el diccionario a buscar si se encuentra
                matcheando el nombre.
    Retorna un booleano que verifica el exito o no de la funcion, es decir, si encontró el diccionario.
    '''

    encontrado = False
    
    proyecto_a_buscar = input("Ingrese el nombre del proyecto: ")

    for diccionario in lista_diccionarios:
        for clave in diccionario:
            if clave == "Nombre del Proyecto":
                if diccionario[clave] == proyecto_a_buscar:
                    encontrado = True
                    diccionario_a_buscar.update(diccionario)
                    break
    
    return encontrado
        
def calcular_promedio (lista_diccionarios: list):
    '''
    Funcion que calcula el promedio del presupuesto de todos los proyectos existentes.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    Retorna la lista de diccionarios o un booleano (Si la lista está vacía)
    '''
    acumulador_proyecto = 0

    if lista_diccionarios:
        for key, diccionario in enumerate(lista_diccionarios):
            for key in diccionario:
                if key == "Presupuesto":
                    acumulador_proyecto += int(diccionario [key])
        
        promedio = float(round(acumulador_proyecto/len(lista_diccionarios),2))
        return promedio
    else:
        return False
    
def comprobar_proyectos (lista_diccionarios: list) -> bool:
    '''
    Funcion que se encarga de comprobar que los proyectos cuya fecha de finalización 
    haya sucedido, tenga su respectivo estado como "Finalizado". Se fija si la lista está vacía o no.
    Se utiliza la biblioteca datetime para convertir la fecha y verificar si la fecha actual
    es mayor a la fecha de fin.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    Retorna un booleano que verifica el exito o no de la funcion.
    '''

    #Defino cual es la fecha de hoy para realizar la comparación.
    fecha_actual = datetime.now()
    
    if lista_diccionarios:
        for diccionario in lista_diccionarios:
            fecha_fin = datetime.strptime(diccionario["Fecha de Fin"], "%d-%m-%Y")
            if fecha_fin < fecha_actual and diccionario ["Estado"] == "Activo":
                diccionario["Estado"] = "Finalizado"
        return True
    else:
        return False

def retomar_proyecto (lista_diccionarios: list) -> int:
    '''
    Funcion que se encarga de retomar proyectos que estén cancelados. Primero verifica que se ingrese el ID
    por parte del usuario y que este coincida con los de la lista de proyectos.
    Si no coincide, informará que en realidad esta activo o finalizado el proyecto.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    Retorna una constante que verifica el exito o no de la funcion. El retorno puede ser correcto, cancelado,
    o erroneo si es que no se encontró el proyecto.
    '''
    retorno = RETOMAR_ERRONEO

    mostrar_todos (lista_diccionarios)

    #Programar que encuentre el ID
    while True:
        try:
            id_a_retomar = int(input("Ingrese el ID del proyecto a retomar: "))
            break
        except ValueError:
            print("Formato no válido... ")
    
    indice = buscar_proyecto(lista_diccionarios,id_a_retomar)

    if indice!= None:
        if lista_diccionarios[indice]["Estado"] == "Cancelado":
            confirma = confirmar_accion("¿Desea confirmar el alta de nuevo(S/N)?: ","ERROR/Solo se acepta S/N. ¿Desea confirmar el alta (S/N): ")

            if confirma:
                lista_diccionarios[indice]["Estado"] = "Activo"
                retorno = RETOMAR_CORRECTO
            else:
                retorno = RETOMAR_CANCELADO
        elif lista_diccionarios[indice]["Estado"] == "Activo":
            print("Ese proyecto esta activo actualmente.")
            retorno = RETOMAR_CANCELADO
        else:
            fecha_fin = datetime.strptime(lista_diccionarios[indice]["Fecha de Fin"], "%d-%m-%Y")
            fecha_hoy = datetime.now()

            if fecha_fin > fecha_hoy:
                confirma = confirmar_accion("¿Desea confirmar el alta de nuevo(S/N)?: ","ERROR/Solo se acepta S/N. ¿Desea confirmar el alta (S/N): ")
                if confirma:
                    lista_diccionarios[indice]["Estado"] = "Activo"
                    retorno = RETOMAR_CORRECTO
                else:
                    retorno = RETOMAR_CANCELADO
            else:
                print("Ese proyecto ya finalizo.")
                retorno = RETOMAR_CANCELADO

    return retorno
                    
def modificar_proyecto (lista_diccionarios: list):
    '''
    Funcion que se encarga de modificar proyecto siempre y cuando matchee con los ID de la lista.
    Primero verifica que la lista esté vacía, de lo contrario lo informará por consola.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    No retorna nada.
    '''
    
    if lista_diccionarios:
        id_encontrado = False

        mostrar_todos (lista_diccionarios)

        while True:
            try:
                id_a_modificar = int(input("Ingrese el ID del proyecto a modificar: "))
                break
            except ValueError:
                print("Formato no válido... ")

        #Aqui verifica si está o no el ID.
        for diccionario in lista_diccionarios:
            if int(diccionario["id"]) == id_a_modificar:
                id_encontrado = True
                break
        
        for diccionario in lista_diccionarios:
            if id_encontrado:
                if int(diccionario["id"]) == id_a_modificar:
                    while True:
                        opcion = ingresar_entero ("""Opciones:
                            1-Nombre Proyecto
                            2-Descripcion
                            3-Fecha Inicio y Fin
                            4-Presupuesto
                            5- Salir
                            Ingrese opcion: """, "Error. Ingrese nuevamente", 1,5)
                        match opcion:
                            case 1:
                                nombre = ingresar_string_nombre("Ingrese nombre a modificar: ", "Error. Ingrese nuevamente: ")
                                diccionario["Nombre del Proyecto"] = nombre
                                pass
                            case 2:
                                descripcion = ingresar_descripcion("Ingrese descripcion a modificar: ", "Error. Ingrese nuevamente: ")
                                diccionario["Descripción"] = descripcion
                                pass
                            case 3:
                                lista_con_fechas = ingresar_validar_fechas()
                                fecha_inicio = lista_con_fechas[0]
                                fecha_fin = lista_con_fechas[1]
                                diccionario["Fecha de inicio"] = fecha_inicio
                                diccionario["Fecha de Fin"] = fecha_fin
                                pass
                            case 4:
                                presupuesto = ingresar_presupuesto("Ingrese presupuesto: (minimo $500000)", "Error, presupuesto invalido",
                                        500000)
                                diccionario["Presupuesto"] = str(presupuesto)
                                pass
                            case 5:
                                print("Fin de la modificación.")
                                os.system('cls')
                                break
            else:
                print("No se encontro ese proyecto.") #Si no lo encuentra, vuelve al menu principal.
                break
    else:
        print("La lista está vacía...")
    
def dar_de_baja_proyecto(lista_diccionarios:list) -> bool:
    '''
    Funcion que se encarga de dar de baja solamente los proyectos ACTIVOS.
    Cambia el estado a Cancelado cuando el usuario lo confirma.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    Retorno: devuelve enteros. Será una "baja correcta" si se logró la baja
    del proyecto, "erronea" si es que no encontró el ID o "cancelada"
    si el usuario se arrepintió.

    '''

    retorno = BAJA_ERRONEA
    
    mostrar_todos (lista_diccionarios)

    while True:
        try:
            id_a_borrar = int(input("Ingrese el ID del proyecto a dar de baja: "))
            break
        except ValueError:
            print("Formato no válido... ")

    indice = buscar_proyecto(lista_diccionarios,id_a_borrar)
    
    if indice != None:
        if lista_diccionarios[indice]["Estado"] == "Activo":
            confirma = confirmar_accion("¿Desea confirmar la baja (S/N): ",
                                        "ERROR/Solo se acepta S/N. ¿Desea confirmar la baja (S/N): ")   
    
            #BAJA LOGICA 
            if confirma:
                lista_diccionarios[indice]["Estado"] = "Cancelado"
                retorno = BAJA_CORRECTA
            else:
                retorno = BAJA_CANCELADA
        elif lista_diccionarios[indice]["Estado"] == "Cancelado":
            print("Ese proyecto esta cancelado actualmente.")
            retorno = RETOMAR_CANCELADO
        else:
            print("Ese proyecto ya finalizo.")
            retorno = RETOMAR_CANCELADO
            
    return retorno

def buscar_proyecto(lista_diccionarios:list,id_a_buscar)-> int:   
    '''
    Funcion que busca el indice del proyecto y si matchea con lo ingresado por el usuario.
    Recibe la lista de diccionarios y el id a buscar.
    Devuelve el indice si lo encontró o un None.
    '''
    
    indice = None 
    
    for i in range(len(lista_diccionarios)):
        if id_a_buscar == int(lista_diccionarios[i]["id"]):
            indice = i
            break
        
    return indice

def contar_dicts_activos(lista_diccionarios)-> int:
    '''
    Funcion que cuenta la cantidad de proyectos activos actualmente.
    Se utiliza para ver si se alcanzó el límite de 50 proyectos activos y 
    para poder cancelar algún proyecto elegido por el usuario.
    Recibe la lista de diccionarios.
    Devuelve la cantidad de diccionarios activos.
    '''
    
    contador = 0
    
    for diccionario in lista_diccionarios:
        if diccionario["Estado"] == "Activo":
            contador+=1
            
    return contador   

def ingresar_validar_fechas () -> list:
    '''
    Funcion que solicitará el ingreso de fechas de inicio y fin por parte de la funcion que ingresa
    proyectos. Se utiliza la libreria datetime para convertirlas a formato fecha y comparar 
    que la de inicio no sea mayor a la de fin.
    Parametros: lista_diccionarios (list): Una lista que contiene diccionarios.
    Retorna una lista con dos fechas en formato string: de inicio y de fin.
    '''

    while True:
        #Ingreso de fechas
        print("Fecha de inicio:\n")
        fecha_inicio = ingresar_fecha("Error, entero invalido")
        print("Fecha de fin:\n")
        fecha_fin = ingresar_fecha ("Error, entero invalido")

        #Intento pasar a formato fecha con la libreria datetime lo ingresado por el usuario (previamente validado)
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y")
            fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y")
        except ValueError:
            print("Error de formato... ")
            continue

        #Aqui confirmo que la fecha de inicio no sea mayor a la de fin
        #y en caso contrario vuelvo solicitar fechas
        if fecha_inicio > fecha_fin:
            print("EL AÑO NO DE INICIO NO PUEDE SER MAYOR AL DE FIN\nDebe" 
                 "reintroducir fecha!!")
        else:
            break
    
    #Cambio a formato string las fechas para luego agregarlas a la lista de fechas y 
    #retornar ambas.
    #Ambas fechas están en formato 'dia-mes-año'
    fecha_inicio_formateada = fecha_inicio.strftime("%d-%m-%Y")
    fecha_fin_formateada = fecha_fin.strftime("%d-%m-%Y")

    retorno_fechas = []
    retorno_fechas.append(fecha_inicio_formateada)
    retorno_fechas.append(fecha_fin_formateada)

    return retorno_fechas

def ingresar_proyecto (id_auto_incremental: int, lista_diccionarios: list)-> bool:
    '''
    Funcion que se encarga de pedir los datos para el ingreso del proyecto.
    Valida que cada valor esté dentro de los parámetros establecidos.
    Agrega el diccionario a la lista de diccionarios auxiliares.
    Parametros: recibe el id auto incremental seteado por default en 10 y la lista de diccionarios.
    Retorna un booleano que verifica el exito o no de la funcion.
    '''
    
    retorno = False

    nombre_proyecto = ingresar_string_nombre("Ingrese un nombre: ", "ERROR/Reingrese un nombre: ")
    descripcion = ingresar_descripcion("Ingrese descripcion: ","ERROR/Reingrese descripcion: " )

    #Validacion y solicitud de fechas
    lista_con_fechas = ingresar_validar_fechas ()

    fecha_inicio = lista_con_fechas[0]
    fecha_fin = lista_con_fechas[1]

    presupuesto = ingresar_presupuesto("Ingrese presupuesto(minimo $500000): ", "Error, presupuesto invalido",
                                       500000)
    
    estado = "Activo"
    
    proyecto = {"id": str(id_auto_incremental), "Nombre del Proyecto": nombre_proyecto, "Descripción": descripcion,
                "Fecha de inicio": fecha_inicio, "Fecha de Fin": fecha_fin, "Presupuesto": str(presupuesto), 
                "Estado": estado}

    confirma = confirmar_accion("¿Desea confirmar el alta (S/N): ","ERROR/Solo se acepta S/N. ¿Desea confirmar el alta (S/N): ")

    if confirma:
        lista_diccionarios.append(proyecto)
        retorno = True
    
    return retorno

