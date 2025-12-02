#*************** Zona de Funciones ***************#

def pedir_longitud():
    longitud = float(input("Ingrese la longitud de la base: "))
    return longitud

def pedir_altura():
    altura = float(input("Ingrese la altura: "))
    return altura

def pedir_ancho():
    ancho = float(input("Ingrese el ancho: "))
    return ancho

def calcular_volumen(longitud, altura, ancho):
    volumen = (1/2 * ancho * altura)* longitud
    return volumen

def imprimir_resultado(resultado_volumen):
    print("El volumen del prisma triangular es: ", resultado_volumen)
    
#*************** Codigo Principal de Python ***************#
longitud = pedir_longitud()
altura = pedir_altura()
ancho = pedir_ancho()
volumen = calcular_volumen(longitud, altura, ancho)
resultado = imprimir_resultado(volumen)