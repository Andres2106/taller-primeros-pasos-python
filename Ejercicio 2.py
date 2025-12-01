#**********  Zona de Función  ***********#


def definir_pi():
    pi= 3.1416
    return pi


def definir_radio():
    radio= 43
    return radio


def calcular_volumen (pi, radio):
    volumen = (radio**3 * pi)*4/3
    return volumen


def imprimir_resultado(resultado_volumen):
    print("El volumen de la esfera es de: ", int(resultado_volumen))


#**************** Codigo Principal Python ****************#

pi= definir_pi()
radio= definir_radio()
volumen= calcular_volumen(pi, radio)
resultado= imprimir_resultado(volumen)