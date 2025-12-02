#*************** Zona de Funciones ***************#

def definir_base():
    base = 6
    return base

def definir_altura():
    altura = 5
    return altura

def calcular_area(base, altura):
    area = (base * altura)
    return area

def Imprimir_resultado(resultado_area):
    print("El area del paralelogramo es: " +str(resultado_area))
    
#*************** Codigo Principal de Python ***************#
base = definir_base()
altura = definir_altura()
area = calcular_area(base, altura)
resultado = Imprimir_resultado(area)