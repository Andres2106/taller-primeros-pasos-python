#************ Zona de Funciones ************#

def pedir_numero1():
    entero1 = int(input("Ingrese el primer número: "))
    return numero1

def pedir_numero2():
    entero2 = int(input("Ingrese el segundo número: "))
    return numero2

def calcular_promedio(numero1, numero2):
    promedio = (numero1 + numero2)/2
    return promedio

def Imprimir_resultado(resultado_promedio):
    print("El promedio de ambos números es: ", str(resultado_promedio))

#************ Codigo Principal de Python ************#
numero1 = pedir_numero1()
numero2 = pedir_numero2()
promedio = calcular_promedio(numero1, numero2)
resultado = Imprimir_resultado(promedio)