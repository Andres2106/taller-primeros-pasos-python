#************ Zona de Funciones ************#

def pedir_dinero():
    dinero = float(input("Ingrese la cantidad de dinero: "))
    return dinero

def pedir_tiempo():
    tiempo = float(input("Ingrese la cantidad de tiempo: "))
    return tiempo

def definir_interes():
    interes = 0.05
    return interes

def calcular_total(dinero, tiempo, interes):
    tasa = (dinero * interes * tiempo)
    total = (dinero + tasa)
    return total

def Imprimir_resultado(resultado_interes):
    print("La tasa de interes es: ", str(resultado_interes))

#************ Codigo Principal de Python ************#
dinero = pedir_dinero()
tiempo = pedir_tiempo()
interes = definir_interes()
total = calcular_total(dinero, tiempo, interes)
resultado = Imprimir_resultado(total)