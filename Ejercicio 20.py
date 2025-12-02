#*************** Zona de Funciones ***************#

def pedir_litro():
    litro = float(input("Ingrese la cantidad de litros: "))
    return litro

def calcular_galones(litro):
    galon = 0.264172
    conversion = (litro * galon)
    return conversion

def imprimir_resultado(resultado_conversion):
    print("La conversion de litro a galon es: ", resultado_conversion)
    
#*************** Codigo Principal de Python ***************#
litro = pedir_litro()
conversion = calcular_galones(litro)
resultado = imprimir_resultado(conversion)