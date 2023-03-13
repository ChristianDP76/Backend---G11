class Persona:
    # Cuando una variable se define dentro de una clase pasa a llamarse 'ATRIBUTO'
    estatura = 1.80
    peso = 80
    signo_zodiacal = 'Leo'

    def sumar(self, *args):
        # self es como el 'this' en el caso de js, c#, c++
        # cuando una funcion se declara o se define dentro de una clase pasa a llamarse "METODO"
        # Recibir un número ilimitado de numeros para realizar su sumatoria
        total = 0
        for numero in args:
            total = total + numero
        return total
    
    def saludar(self, nombre):
        return 'hola {}'.format(nombre)
    
# Cuando sacamos una 'copia' de la Clase para utilizarla estamos creando una "INSTANCIA"
persona1 = Persona()
persona2 = Persona()

persona1.peso=70
persona2.peso=50

# Todas las modificaciones que hacemos es independiente de la 'Instancia'
print(persona1.peso)
print(persona2.peso)


resultado1 = persona1.sumar(10,5,41,526,489,63)
resultado2 = persona2.sumar(5,8,65,985,492,520,700)

print(resultado1)
print(resultado2)
