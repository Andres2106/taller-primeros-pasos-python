#**********  Zona de Función  ***********#

def definir_grados():
    grados= 33
    return grados


def calcular_Fahrenheit(grados):
    Fahrenheit= (grados * (9/5) + 32)
    return Fahrenheit


def imprimir_resultado(resultado_Fahrenheit):
    print("La conversión de grados Celcius a Fahrenheit es: " + str(resultado_Fahrenheit))
    
    
#**************** Codigo Principal Python ****************#


grados = definir_grados()
Fahrenheit = calcular_Fahrenheit(grados)
resultado = imprimir_resultado(Fahrenheit)