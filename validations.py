'''
Funciones donde se encuentran las validaciones de cada dato (nombre, descripcion, fecha, etc)
'''

from project_functions import *
from main import *
from datetime import datetime


def ingresar_entero(mensaje:str,mensaje_error:str,minimo:int,maximo:int)-> int:
    '''
    Funcion que se encarga de pedir un entero y validarlo con un try/except
    si está dentro de los minimo y maximo parametros recibidos.
    Parametros: un mensaje solicitando numeros, un mensaje de error por si es incorrecta la entrada,
    un maximo y un minimo numero.
    Retorno: devuelve el entero validado.
    '''
    while True:
        try: 
            dato_entero = int(input(mensaje))
            if dato_entero <= maximo and dato_entero >= minimo:
                break
            else:
                print(mensaje_error)
        except ValueError:
            print("Formato no válido... ")

    return dato_entero

def ingresar_string_nombre(mensaje: str, mensaje_error: str) -> str:
    '''
    Funcion que se encarga de pedir el nombre del proyecto validando que 
    no pase de 30 caracteres y que sea alfabético el dato.
    Parametros: un mensaje solicitando el nombre del proyecto y un mensaje de error 
    por si es incorrecta la entrada.
    Retorno: devuelve el nombre del proyecto validado.
    '''
    
    while True:
        dato_ingresado = input(mensaje)
        if len(dato_ingresado) <= 30 and dato_ingresado.replace(" ", "").isalpha():
            return dato_ingresado
        
        print(mensaje_error)

def ingresar_descripcion(mensaje: str, mensaje_error: str) -> str:
    '''
    Funcion que se encarga de pedir la descripción del proyecto validando que 
    no pase de 200 caracteres y que sea alfanumérico el dato.
    Parametros: un mensaje solicitando la descripción del proyecto y un mensaje de error 
    por si es incorrecta la entrada.
    Retorno: devuelve la descripción del proyecto validado.
    '''

    while True:
        dato_ingresado = input(mensaje)
        if len(dato_ingresado) <= 200 and dato_ingresado.replace(" ", "").isalnum():
            return dato_ingresado
        
        print(mensaje_error)

def ingresar_presupuesto(mensaje:str,mensaje_error:str,minimo:int)-> int:
    '''
    Funcion que se encarga de pedir el presupuesto del proyecto validando con un try/except que 
    cumpla con el presupuesto mínimo solicitado.
    Parametros: un mensaje solicitando el presupuesto del proyecto y un mensaje de error 
    por si es incorrecta la entrada.
    Retorno: devuelve el presupuesto del proyecto validado.
    '''   
    
    while True:
        try: 
            dato_presupuesto = int(input(mensaje))
            if dato_presupuesto >= minimo:
                break
            else:
                print(mensaje_error)
        except ValueError:
            print("Formato no válido... ")

    return dato_presupuesto

def ingresar_fecha(mensaje_error)-> str:
    '''
    Funcion que solicita ingresar dia, mes y año de fecha de inicio/fin 
    y valida los formatos correctos de cada uno.
    Recibe el mensaje de error por si es incorrecta la entrada de cada uno.
    Retorna la fecha formateada a string.
    '''

    #dia
    while True:
        try: 
            dia = int(input("Ingrese el dia: "))
            if dia <= 31 and dia >= 1:
                break
            else:
                print(mensaje_error)
        except ValueError:
            print("Formato no válido... ")

    #mes
    while True:
        try: 
            mes = int(input("Ingrese el mes: "))
            if mes <= 12 and mes >= 1:
                break
            else:
                print(mensaje_error)
        except ValueError:
            print("Formato no válido... ")

    #año
    while True:
        try: 
            año = int(input("Ingrese el año (mayor o igual a 2000): "))
            if año <= 2100 and año >= 2000:
                break
            else:
                print(mensaje_error)
        except ValueError:
            print("Formato no válido... ")

    #Retorno la fecha (inicio o fin) en forma de string. 
    fecha = f'{dia}-{mes}-{año}'

    return fecha


def confirmar_accion(mensaje:str,mensaje_error:str)-> bool:
    '''
    Funcion que confirma la accion del usuario mediante un S o N (si o no).
    Recibe un mensaje si desea confirmar la accion y uno de error
    si la respuesta fue incorrecta.
    Retorna un booleano True si el dato es "si" o False si es "no".
    '''
    
    confirmar = input(mensaje)
    
    while confirmar != "S" and confirmar != "N":
        confirmar = input(mensaje_error)
    
    if confirmar == "S":
        retorno = True
    else:
        retorno = False
        
    return retorno