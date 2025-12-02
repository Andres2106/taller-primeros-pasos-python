#*************** Zona de Funciones ***************#

def pedir_libras():
    libras = float(input("Ingrese la cantidad de libras: "))
    return libras

def calcular_kilogramos(libras):
    kilogramo = 0.453592
    conversion = (libras * kilogramo)
    return conversion

def imprimir_resultado(resultado_conversion):
    print("La conversion de libras a kilogramos es: ", resultado_conversion)

#*************** Codigo Principal de Python ***************#
libras = pedir_libras()
conversion = calcular_kilogramos(libras)
resultado = imprimir_resultado(conversion)