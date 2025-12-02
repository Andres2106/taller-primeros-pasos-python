#*************** Zona de Funciones ***************#

def pedir_numero():
    numero = float(input("Ingrese un numero: "))
    return numero

def calcular_numeros(numero):
    raiz = numero**2
    return raiz

def imprimir_resultado(resultado_raiz):
    print("El resultado de la raiz cuadrada del numero es: ", resultado_raiz)
    
#*************** Codigo Principal de Python ***************#
numero = pedir_numero()
raiz = calcular_numeros(numero)
resultado = imprimir_resultado(raiz)