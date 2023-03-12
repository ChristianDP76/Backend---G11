# def suma(a, b):
#     print(b)
# 
# suma(2, 3)

def suma(a, b):
    return a + b

#resultado_suma = suma(3, 3)
#print(resultado_suma)

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def calcularResultadoporOperacion(operacion, valor1, valor2):
    if operacion == 'suma':
        return f'El resultado de la {operacion} es: {suma(valor1, valor2)}'
    elif operacion == 'resta':
        return f'El resultado de la {operacion} es: {resta(valor1, valor2)}'
    else:
        return 'La Operación no Existe'

operacion = input('Ingrese el tipo de Operación: ')
valor_1= int(input('Ingrese el Primer número: '))
valor_2= int(input('Ingrese el Segundo número: '))

resultado =calcularResultadoporOperacion(operacion, valor_1, valor_2)
print(resultado)

# --- 'f' Método Format
# nombre = input('Ingrese su nombre: ')
# Edad = input('Ingrese su Edad: ')
# print(f'Hola {nombre}, tu tienes {Edad} años')







