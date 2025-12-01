#**********  Zona de Función  ***********#


def definir_longitud():
    longitud= 18
    return longitud


def definir_ancho():
    ancho= 25
    return ancho


def calcular_area(ancho, longitud):
    area = (ancho*longitud)/2
    return area

def imprimir_resultado(resultado_area):
    print("El área del rectángulo es: " + str(resultado_area))
    

#**************** Codigo Principal Python ****************#


longitud = definir_longitud()
ancho = definir_ancho()
area = calcular_area(ancho, longitud)
resultado = imprimir_resultado(area)