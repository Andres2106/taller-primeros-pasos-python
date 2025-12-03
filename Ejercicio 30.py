#*************** Zona de Funciones ***************#

def pedir_radio():
    radio = float(input("Ingrese el radio: "))
    return radio

def definir_pi():
    pi = 3.14
    return pi

def calcular_circ(radio, pi):
    circunferencia = (2 * pi * radio)
    return circunferencia

def Imprimir_resultado(resultado_circ):
    print("La circunferencia es: ", str(resultado_circ))

#*************** Código Principal de Python ***************#
radio = pedir_radio()
pi = definir_pi()
circunferencia = calcular_circ(radio, pi)
resultado = Imprimir_resultado(circunferencia)