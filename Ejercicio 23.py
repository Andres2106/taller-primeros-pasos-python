#*************** Zona de Funciones ***************#

def pedir_numero1():
    numero1 = float(input("Ingrese un numero: "))
    return numero1

def pedir_numero2():
    numero2 = float(input("Ingrese otro numero: "))
    return numero2

def calcular_numeros(numero1, numero2):
    mult = numero1 * numero2
    return mult

def imprimir_resultado(resultado_mult):
    print("El resultado de la multiplicación es: ", resultado_mult)
    
#*************** Codigo Principal de Python ***************#
numero1 = pedir_numero1()
numero2 = pedir_numero2()
mult = calcular_numeros(numero1, numero2)
resultado = imprimir_resultado(mult)