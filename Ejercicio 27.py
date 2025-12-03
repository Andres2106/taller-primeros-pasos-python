#*************** Zona de Funciones ***************#

import math

def pedir_num():
    num = int(input("Ingrese su numero: "))
    return num


def calcular_raiz_cuadrada(num):
    raiz= (math.sqrt(num))
    return raiz


def Imprimir_resultado(resultado_raiz):
    print("La raiz cuadrada del numero es: ", str(resultado_raiz))

#*************** Código Principal de Python ***************#
num = pedir_num()
raiz = calcular_raiz_cuadrada(num)
resultado = Imprimir_resultado(raiz)