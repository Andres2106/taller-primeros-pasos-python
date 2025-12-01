#**********  Zona de Función  ***********#

def definir_pi():
    pi=3.1416
    return pi


def definir_radio():
    radio= 45
    return radio


def definir_altura():
    altura= 26
    return altura


def calcular_volumen(pi, radio, altura):
    volumen= (pi* radio**2 * altura)
    return volumen


def imprimir_resultado(resultado_volumen):
    print("El volumen del cilindro es: " +str(resultado_volumen))


#**************** Codigo Principal Python ****************#


pi= definir_pi()
radio= definir_radio()
altura= definir_altura()
volumen= calcular_volumen(pi, radio, altura)
resultado= imprimir_resultado(volumen)    