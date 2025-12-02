#*************** Zona de Funciones ***************#

def pedir_pulgadas():
    pulgadas = float(input("Ingrese las pulgadas: "))
    return pulgadas

def calcular_centimetros(pulgadas):
    centimetros = 2.54
    conversion = (pulgadas * centimetros)
    return conversion

def imprimir_resultado(resultado_conversion):
    print("El resultado de la conversion de pulgadas a centímetros es: ", resultado_conversion)

#*************** Codigo Principal de Python ***************#
pulgadas = pedir_pulgadas()
conversion = calcular_centimetros(pulgadas)
centimetros = imprimir_resultado(conversion)