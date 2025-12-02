#*************** Zona de Funciones ***************#

def pedir_numero1():
    numero1 = float(input("Ingrese un numero: "))
    return numero1

def pedir_numero2():
    numero2 = float(input("Ingrese otro numero: "))
    return numero2

def calcular_numeros(numero1, numero2):
    resta = numero1 - numero2
    return resta

def imprimir_resultado(resultado_resta):
    print("El resultado de la resta es: ", resultado_resta)
    
#*************** Codigo Principal de Python ***************#
numero1 = pedir_numero1()
numero2 = pedir_numero2()
resta = calcular_numeros(numero1, numero2)
resultado = imprimir_resultado(resta)