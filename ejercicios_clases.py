# Crear una Clase Operaciones con sus respectivos métodos
# METODOS: Sumar - Restar - Multiplicar - Dividir
# Esta clase recibirá 2 parámetros

class OperacionesMatematicas:
    def __init__(self, valor1, valor2):
        self.a = valor1
        self.b = valor2

    def Suma(self):
        return self.a + self.b
    
    def Resta(self):
        return self.a - self.b
    
    def Multiplicacion(self):
        return self.a * self.b
    
    def Dividir(self):
        return self.__redondear(self.a / self.b)
    
    # Método Privado '__Redondear' 
    def __redondear(self, numero):
        return round(numero, 2)
        

Opera = OperacionesMatematicas(5, 4)

print(Opera.Dividir())


    

        
