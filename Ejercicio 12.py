#*************** Zona de Funciones ***************#

def pedir_lado():
    lado = float(input("Ingrese un lado del cuadrado: "))
    return lado

def calcular_area(lado):
    area = (lado**2)
    return area

def imprimir_resultado(resultado_area):
    print("El area del cuadrado es: ", resultado_area)
    
#*************** Codigo Principal de Python ***************#
lado = pedir_lado()
area = calcular_area(lado)
resultado = imprimir_resultado(area)