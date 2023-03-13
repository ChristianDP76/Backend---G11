class Producto:
    def __init__(self, nombre, precio, cantidad, fecha_Vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fVencimiento = fecha_Vencimiento
        # --atributo > privado > significa que no se puede acceder a esta información desde fuera de la clase
        self.__Ganancia = 0.3

    def prueba(self):
        self.__Ganancia
        print(self.__Ganancia)

pitahaya = Producto('Pitahaya', 4.50, 100, '2023-02-22')
print(pitahaya.nombre)

pitahaya.prueba()





        