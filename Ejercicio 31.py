#*************** Zona de Funciones ***************#

def pedir_horas():
    horas = float(input("Ingrese las horas: "))
    return horas

def calcular_minutos(horas):
    minutos= (horas*60)
    return minutos

def Imprimir_resultado(resultado_minutos):
    print("La conversión de horas es: ", str(resultado_minutos))

#*************** Código Principal de Python ***************#
horas = pedir_horas()
minutos = calcular_minutos(horas)
resultado = Imprimir_resultado(minutos)