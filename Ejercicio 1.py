#**********  Zona de Función  ***********#

def definir_altura():
    altura_t = 12
    return altura_t

def definir_base():
    base_t = 15
    return base_t

def calcular_area(base, altura):
    area = (base*altura)/2
    return area

def imprimir_datos(base_t, altura_t):
    mensaje = "La base es: " +base_t
    mensaje = "La altura es: " +altura_t

def imprimir_resultado(resultado_area):
    print("El área del triángulo es: " + str(resultado_area))

#**************** Codigo Principal Python ****************#

base = definir_base()
altura = definir_altura()
area = calcular_area(base, altura)
resultado = imprimir_resultado(area)