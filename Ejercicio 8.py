#**********  Zona de Función  ***********#

def definir_dolares():
    dolares= 100
    return dolares

def definir_tasa_cambio():
    tasa_cambio= 0.92
    return tasa_cambio

def calcular_equivalente(dolares, tasa_cambio):
    Equivalente= (dolares * tasa_cambio)
    return Equivalente


def imprimir_resultado(resultado_equivalente):
    print("La conversión de dolares a euros es: " + str(resultado_equivalente))
    
    
#**************** Codigo Principal Python ****************#


dolares = definir_dolares()
tasa_cambio = definir_tasa_cambio()
Equivalente = calcular_equivalente(dolares, tasa_cambio)
resultado = imprimir_resultado(Equivalente)