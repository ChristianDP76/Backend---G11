# con 'self' nos permite acceder al contenido de una CLASE.
# metodos magicos '__init__' permite extraer o recibir los valores que le estamos dando a nuestra clase

class Vehiculo:
    def __init__(self, color, placa, marca) -> None:
        self.color = color
        self.placa = placa
        self.marca = marca
    
    def verificarEstado(self, fabricacion):
        return f'El vehiculo de color {self.color} fue fabricado en el año: {fabricacion}'
    
    def concatenarCaracteristicas(self):
        return f'El vehículo con placa {self.placa} y de color {self.color} es de marca: {self.marca}'

vehiculo = Vehiculo("rojo","V21-543", "Honda")

#print(vehiculo.verificarEstado(1999))
#print(vehiculo.concatenarCaracteristicas())

# -- Usando el método '__str__' nos retorna un valor a esa clase
class Alumno:
    def __init__(self, nomb, ed) -> None:
        self.nombre = nomb
        self.edad = ed

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    
    def mostrarNombre(self):
        return self.nombre
    
    def mostrarEdad(self):
        return self.edad


x = Alumno('Christian', 30)

print(x.mostrarNombre())


    