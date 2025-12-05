#*************** Zona de Funciones **************#
suma = 0
for i in range(0,10):
    numero = int(input("Digite el numero " +str(i+1)+": "))
    suma = suma +  numero

def Imprimir_resultado(resultado_suma):
    print("La sumatoria total es: " +str(resultado_suma))

#*************** Código Principal de Python ***************#
resultado = Imprimir_resultado(suma)