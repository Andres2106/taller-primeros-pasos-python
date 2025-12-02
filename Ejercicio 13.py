#*************** Zona de Funciones ***************#

def pedir_longitud():
   longitud = float(input("Ingrese la longitud de la base: "))
   return longitud

def pedir_ancho():
    ancho = float(input("Ingrese el ancho de la base: "))
    return ancho

def pedir_altura():
    altura = float(input("Ingrese la altura de la pirámide: "))
    return altura

def calcular_volumen(longitud, ancho, altura):
    volumen = (longitud * ancho * altura)/3
    return volumen

def imprimir_resultado(resultado_volumen):
    print("El volumen de la pirámide es: ", resultado_volumen)
    
#*************** Codigo Principal de Python ***************#
longitud = pedir_longitud()
ancho = pedir_ancho()
altura = pedir_altura()
volumen = calcular_volumen(longitud, ancho, altura)
resultado = imprimir_resultado(volumen)