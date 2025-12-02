#*************** Zona de Funciones ***************#

def definir_kilometros():
    kilometros = float (input("Ingrese los kilometros a convertir: "))
    return kilometros

def convertir_millas(kilometros):
    milla=  0.621371
    conversion = (kilometros * milla)
    return conversion

def imprimir_resultado(resultado_conversion):
    print ("El resultado de la conversion de km a millas es: ", resultado_conversion)
    
#*************** Codigo Principal de Python ***************#
kilometros = definir_kilometros()
conversion = convertir_millas(kilometros)
millas = imprimir_resultado(conversion)