# con 'self' nos permite acceder al contenido de una CLASE.
# 

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

print(vehiculo.verificarEstado(1999))
print(vehiculo.concatenarCaracteristicas())



    