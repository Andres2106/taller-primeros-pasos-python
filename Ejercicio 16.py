#*************** Zona de Funciones ***************#

def pedir_longitud():
    longitud = float(input("Ingrese la longitud del lado: "))
    return longitud

def calcular_volumen(longitud):
    volumen = (longitud**3)
    return volumen

def Imprimir_resultado(resultado_volumen):
    print("El volumen del cubo es: ", resultado_volumen)
    
#*************** Codigo Principal de Python ***************#
longitud = pedir_longitud()
volumen = calcular_volumen(longitud)
resultado = Imprimir_resultado(volumen)