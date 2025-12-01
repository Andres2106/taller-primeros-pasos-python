#**********  Zona de Función  ***********#


def definir_pi():
    pi= 3.1416
    return pi


def definir_radio():
    radio= 25
    return radio


def calcular_area(pi, radio):
    area= (pi * radio**2)
    return area


def imprimir_resultado(resultado_area):
    print("El area del círculo es: " +str(resultado_area))
    
    
#**************** Codigo Principal Python ****************#

pi = definir_pi()
radio = definir_radio()
area = calcular_area(pi , radio)
resultado = imprimir_resultado(area)