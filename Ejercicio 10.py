#*************** Zona de Funciones ***************#

def definir_altura():
    altura = 6
    return altura


def definir_longitud():
    longitud = 4
    return longitud


def definir_ancho():
    ancho = 8
    return ancho


def calcular_volumen(altura, longitud, ancho):
    volumen = (longitud * ancho * altura)
    return volumen


def imprimir_resultado(resultado_volumen):
    print ("El volumen del prisma rectangular es: " +str(resultado_volumen))
    
#*************** Codigo Principal de Python ***************#
altura = definir_altura()
longitud = definir_longitud()
ancho = definir_ancho()
volumen = calcular_volumen(altura, longitud, ancho)
resultado = imprimir_resultado(volumen)