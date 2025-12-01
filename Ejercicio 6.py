#**********  Zona de Función  ***********#

def definir_pi():
    pi=3.14
    return pi


def definir_radio():
    radio= 10
    return radio


def definir_altura():
    altura= 20
    return altura


def calcular_volumen(pi, radio, altura):
    volumen= (1/3 * pi* radio**2 * altura)
    return volumen


def imprimir_resultado(resultado_volumen):
    print("El volumen del cono es: " +str(resultado_volumen))


#**************** Codigo Principal Python ****************#


pi= definir_pi()
radio= definir_radio()
altura= definir_altura()
volumen= calcular_volumen(pi, radio, altura)
resultado= imprimir_resultado(volumen)    