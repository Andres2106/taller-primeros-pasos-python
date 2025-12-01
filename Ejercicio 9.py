#**********  Zona de Función  ***********#


def definir_longitud_1():
    longitud_1= 18
    return longitud_1


def definir_longitud_2():
    longitud_2 = 22
    return longitud_2


def definir_altura():
    altura= 25
    return altura


def calcular_area(longitud_1, longitud_2, altura):
    area = (longitud_1 + longitud_2 + altura)/2
    return area

def imprimir_resultado(resultado_area):
    print("El área del Trapecio es: " + str(resultado_area))
    

#**************** Codigo Principal Python ****************#


longitud_1 = definir_longitud_1()
longitud_2 = definir_longitud_2()
altura = definir_altura()
area = calcular_area(longitud_1, longitud_2, altura)
resultado = imprimir_resultado(area)