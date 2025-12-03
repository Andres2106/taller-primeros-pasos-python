#*************** Zona de Funciones ***************#
def pedir_base():
    base = float(input("Ingrese la base: "))
    return base

def pedir_altura():
    altura = float(input("Ingrese la altura: "))
    return altura

def calcular_area(base, altura):
    area = (base * altura)/2
    return area

def Imprimir_resultado(resultado_area):
    print("El area del triángulo es: ", str(resultado_area))


#*************** Código Principal de Python ***************#
base = pedir_base()
altura = pedir_altura()
area = calcular_area(base, altura)
resultado = Imprimir_resultado(area)