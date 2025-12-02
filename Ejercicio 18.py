#*************** Zona de Funciones ***************#
def pedir_apotema():
    apotema = float(input("Digite el area del perímetro: "))
    return apotema

def definir_lado():
    lado = 6
    return lado

def calcular_area(lado):
    perimetro= 6 * lado
    area = (perimetro * apotema)/2
    return area

def imprimir_resultado(resultado_area):
    print("El area del hexagono regular es: ", resultado_area)
    
#*************** Codigo Principal de Python ***************#
lado = definir_lado()
apotema = pedir_apotema()
area = calcular_area(lado)
resultado = imprimir_resultado(area)