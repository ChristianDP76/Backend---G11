#--- usando funciones y Diccionarios que estan en una Lista ---#

#- Crear un a funcion que reciba la lista de ciudades y ordenarlos por la cantidad de habitantes de menor a mayor -#

import pprint


ciudades = [
    { 
        'nombre': 'Tumbes',
        'habitantes': 500000
    },
    {
        'nombre': 'Arequipa',
        'habitantes': 800000
    },
    {
        'nombre': 'Loreto',
        'habitantes': 10000
    }
]

#ordenar numeros usando el Método 'SORT'

# lista_numeros.sort()
# lista_numeros = [1,5,2,4,6,9,8]
# print(lista_numeros)


def miFuncion(ciudad):
    return ciudad['habitantes']

ciudades.sort(key=miFuncion, reverse=True)
#- Añadir una lista usando el método .append
ciudades.append({'nombre': 'Cusco','habitantes': 20000})
#ciudades.pop(0)

index = 0
for ciudad in ciudades:
    if ciudad['nombre'] == 'Cusco':
        ciudades.remove(ciudad)
    index= index + 1

print(ciudades)

lista = ['Arequipa', 'Cusco', 'Tumbes']
lista.remove('Arequipa')


# 
# 
#  Eliminando un dato de la Lista usan el método Remove -#
# lista.remove('Arequipa')

# print(lista)









# def ordenarCiudades(Lista_ciudades):
       
    

#ordenarCiudades(ciudades)