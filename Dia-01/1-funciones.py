# Creando Funciones

# def saludar(nombre):
 #    saludo = 'Hola {}'.format(nombre)
 #    print(saludo)

# saludar('Christian')

# def saludar_Varios(*args):
    # cuando nosotros colocamos en un parametro el '*' significa que no hay límite de ese parámetro, este parámetro debe de ir al último
    # Todos los valores que le pasemos a este parámetro se almacenaran en un tupla
    # NOTA: Las tuplas a diferencia de los arreglos no se pueden modificar, osea una vez creadas sus valores no pueden cambiar
#     print(args)
#     for nombre in args:
#         saludo = 'Hola {}'.format(nombre)
#         print(saludo)

# saludar_Varios('Roxana', 'Christian', 'Martin', 'Ricardo', 'Sugey')
# saludar_Varios('Pedro', 'Luis')
# saludar_Varios()
# saludar_Varios('Eduardo', 20, True, 10.5)

# def informacion_usuario(**kwargs):
    # kwargs > keyboard argument o se le pasan parametros por llaves
 #    print(kwargs)
    # .get('llave') > devolver el valor si es que existe la llave, sino existe entonces devolvera None
 #    print(kwargs.get('estatura','No Hay......!'))
 #    try:
 #        print(kwargs['estatura'])
 #    except:
 #        print('No existe la llave estatura')


# informacion_usuario(nombre='Eduardo', edad=30, esta_civil='soltero', estatura=1.70)
# informacion_usuario(nombre='Pamela', apellido= 'Juarez', nacionalidad = 'Colombiana', fecha_nacimiento='31/06/1999')


#------- recibir dos valores y hacer la division (dividendo / divisor) y retornar su resultado ----#

def dividir(dividendo, divisor):
    # Si la división da un error entonces retornar un mensaje que diga 'division incorrecta'
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        # aqui ingresará cuando la división sea entre 0
        return 'No puede haber division entre 0'
    except TypeError:
        # ingresará la división tiene algun carcter
        return 'Las divisiones sólo pueden ser entre Números'
    except:
        # ingresara si no es ninguno de los dos errores anteriores
        return 'Error desconocido'



valor = dividir(10, 0)

print(valor)
valor = dividir('a', 'k')
print(valor)



