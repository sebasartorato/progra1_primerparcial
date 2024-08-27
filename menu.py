'''
Funciones correspondientes al menu y a incrementar/decrementar el ID.
'''
import re

from project_functions import *
from archive_functions import *

#Arranca en 10 porque ya hay cargados por defecto 10 proyectos de antemano.
id_auto_incremental = 10

def incrementar_id():
    '''
    Incrementa el ID en uno cuando se la invoca.
    No recibe ni retorna nada.
    '''
    global id_auto_incremental
    id_auto_incremental +=1
    
def decrementar_id():
    '''
    Decrementa el ID en uno cuando se la invoca.
    No recibe ni retorna nada.
    '''
    global id_auto_incremental
    id_auto_incremental +=-1

def imprimir_menu ():
    '''
    Función que se encarga de imprimir el menú únicamente.
    No recibe ni retorna nada.
    '''
    print('''Bienvenido al menú:
          1. Ingresar proyecto
          2. Modificar proyecto
          3. Cancelar proyecto
          4. Comprobar proyectos
          5. Mostrar todos
          6. Calcular presupuesto promedio
          7. Buscar proyecto por nombre
          8. Ordenar proyectos
          9. Retomar proyecto
          10. Calcular el/los proyectos activos con mayor presupuesto iniciados en otoño. En caso de que no haya indicar error.
          11. Realizar un top 3 de los proyectos finalizados con menor presupuesto. Verificar qué haya la
          cantidad deseada de proyectos , sino indicar un mensaje de error.
          12. Salir
          ''')

def menu (lista_diccionarios: list):
    '''
    Funcion que mediante un while muestra el menú y según lo elegido por el usuario
    ejecuta las funciones.
    Utiliza una expresion regular fijándose que la entrada sea un digito del 1 al 9 
    o un 10.
    Recibe la lista de diccionarios importada desde el csv.
    No retorna nada
    '''
    while True:
        imprimir_menu()
        opcion = 0
        opcion_str = input(f'Ingrese su opcion: ')
        if re.match('^(10|11|12|[1-9])$', opcion_str):
            opcion = int(opcion_str)
        else:
            print("Opcion invalida")

        match (opcion):
            case 1:
                #Ingresar proyecto.
                #Verifico primero que al querer ingresar no se haya alcanzado el limite de 50 proyectos.
                if contar_dicts_activos (lista_diccionarios) == 50:
                    print("Se alcanzó el límite de 50 proyectos activos. Debe finalizar o cancelar uno existente")
                else:
                    incrementar_id()
                    if ingresar_proyecto(id_auto_incremental, lista_diccionarios):
                        print("Se agrego el proyecto. ")
                    else:
                        decrementar_id()
                        print("Operacion Cancelada")
                pass
            case 2:
                #Modificar proyecto.
                modificar_proyecto(lista_diccionarios)
                pass
            case 3:
                #Cancelar proyecto.
                #Aqui se verificara que haya proyectos activos para poder cancelarlos.
                if contar_dicts_activos (lista_diccionarios) > 0:
                    estado_baja = dar_de_baja_proyecto(lista_diccionarios)
                    if estado_baja == BAJA_CORRECTA:
                        print("Se dio de baja correctamente el proyecto")
                    elif estado_baja == BAJA_CANCELADA:
                        print("Se canceló la baja.")
                    else:
                        print("No se encontro el proyecto. Se cancela la baja")
                pass
            case 4:
                #Comprobar proyectos.
                if comprobar_proyectos (lista_diccionarios):
                    print("Se comprobó exitosamente que los proyectos finalizados"
                          " tengan su estado actualizado.")
                else:
                    print("No se pudo actualizar estado por errores en la lista.")
                pass
            case 5:
                #Mostrar proyectos.
                if mostrar_todos(lista_diccionarios):
                    continue
                else:
                    print("Error. No se pudo mostrar la lista")
                pass
            case 6:
                #Calcular promedio presupuesto.
                promedio = calcular_promedio (lista_diccionarios)
                if promedio:
                    print(f"El promedio de todos los presupuestos es de: $ {promedio}\n")
                else:
                    print("Error. No pudo calcularse el promedio")
                pass
            case 7:
                #Buscar proyecto por nombre.
                diccionario_a_buscar = {}
                if buscar_proyecto_nombre(lista_diccionarios, diccionario_a_buscar):
                    print("Proyecto encontrado, encuentre debajo los detalles:")
                    print("-"*50)
                    for key, value in diccionario_a_buscar.items():
                        print(f"| {key}: {value}")
                    print("-"*50)
                else:
                    print("No se pudo obtener ese proyecto")
                pass
            case 8:
                #Ordenar proyectos.
                if ordenar_selection_sort (lista_diccionarios):
                    print("\nOrdenada e impresa con éxito.")
                else:
                    print("\nERROR! No pudo ordenarse/imprimirse.")
                pass
            case 9:
                #Retomar proyectos.
                estado_retomar = retomar_proyecto (lista_diccionarios)
                if estado_retomar == RETOMAR_CORRECTO:
                    print("Se retomó el proyecto exitosamente.")
                elif estado_retomar == RETOMAR_CANCELADO:
                    print("Se cancelo retomar proyecto.")
                else:
                    print("No se encontro el proyecto. Se cancela la baja")
                pass
            case 10:
                #Funcion S
                if calcular_proyectos_activos_otoño(lista_diccionarios):
                    print("Exito en la impresion de la lista\n")
                else:
                    print("Hubo un error, no hay proyectos iniciados en otoño.")
                pass
            case 11:
                #Funcion EXTRA
                contar_finalizados = contar_dicts_finalizados(lista_diccionarios)
                if contar_finalizados > 2:
                    if listar_finalizados_menor_prep(lista_diccionarios):
                        print("Exito en la impresion de la lista\n")
                    else:
                        print("Hubo un error.\n")
                else:
                    print("No hay proyectos finalizados como para calcular top 3.\n")
                pass
            case 12:
                #Salir.
                print("¡Fin del menú!")
                if sobrescribir_csv(lista_diccionarios):
                    print("CSV actualizado.")
                else:
                    print("Error en la actualización del CSV.")
                crear_json_finalizados(lista_diccionarios)
                break
    