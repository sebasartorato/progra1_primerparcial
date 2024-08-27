#1er Parcial
#Sebastian Sartorato

'''
Archivo main donde se llevará a cabo la ejecución del programa.
'''

from menu import *
from project_functions import *
from archive_functions import *

if __name__ == '__main__':
    lista_diccionarios = leer_csv () #Arranco leyendo el CSV y creo la lista de diccionarios
    menu (lista_diccionarios) #Inicio el menú

