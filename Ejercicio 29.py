#*************** Zona de Funciones ***************#
def pedir_num():
    num = float(input("Ingrese su número: ")) 
    return num


def definir_numero(num):
    if num % 2==0:
      return "Par"
    else:
      return "Impar"


def Imprimir_resultado(resultado_num):
    print("El numero ingresado es ", str(resultado_num))

#*************** Código Principal de Python ***************#
num = pedir_num()
definir = definir_numero(num)
resultado = Imprimir_resultado(definir)