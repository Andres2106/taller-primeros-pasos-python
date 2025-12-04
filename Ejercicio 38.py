#************ Zona de Funciones ************#

def pedir_numero1():
    entero1 = int(input("Ingrese el primer número: "))
    return numero1

def pedir_numero2():
    entero2 = int(input("Ingrese el segundo número: "))
    return numero2

def calcular_mayor(numero1, numero2):
    mayor = (numero1 + numero2 + abs(numero1 - numero2))/2
    return mayor

def Imprimir_resultado(resultado_mayor):
    print("El mayor entre ambos números es: ", str(resultado_mayor))

#************ Codigo Principal de Python ************#
numero1 = pedir_numero1()
numero2 = pedir_numero2()
mayor = calcular_mayor(numero1, numero2)
resultado = Imprimir_resultado(mayor)