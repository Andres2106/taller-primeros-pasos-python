#*************** Zona de Funciones ***************#

def pedir_numero():
    numero = float(input("Ingrese un numero: "))
    return numero

def calcular_numeros(numero):
    cuadrado = numero**2
    return cuadrado

def imprimir_resultado(resultado_cuadrado):
    print("El resultado del cuadrado del numero es: ", resultado_cuadrado)
    
#*************** Codigo Principal de Python ***************#
numero = pedir_numero()
cuadrado = calcular_numeros(numero)
resultado = imprimir_resultado(cuadrado)