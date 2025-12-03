#*************** Zona de Funciones ***************#
def pedir_longitud():
    longitud = float(input("Ingrese la longitud: "))
    return longitud

def pedir_ancho():
    ancho = float(input("Ingrese el ancho: "))
    return ancho

def calcular_area(longitud, ancho):
    area = (longitud * ancho)
    return area

def Imprimir_resultado(resultado_area):
    print("El área del rectángulo es: ", str(resultado_area))

#*************** Código Principal de Python ***************#
longitud = pedir_longitud()
ancho = pedir_ancho()
area = calcular_area(longitud, ancho)
resultado = Imprimir_resultado(area)