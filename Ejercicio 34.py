#************ Zona de Funciones ************#

def pedir_precio():
    precio = float(input("Ingrese el precio: "))
    return precio

def definir_descuento():
    descuento = 0.1
    return descuento

def calcular_valor(precio, descuento):
    descuento = (precio * descuento)
    valor_final = (precio - descuento)
    return valor_final

def Imprimir_resultado(resultado_valor):
    print("El valor final con descuento es: ")

#************ Codigo Principal de Python ************#
precio = pedir_precio()
descuento = definir_descuento()
valor_final = calcular_valor(precio, descuento)
resultado = Imprimir_resultado(valor_final)