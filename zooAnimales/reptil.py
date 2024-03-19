from zooAnimales.animal import Animal
class Reptil(Animal):
    
    iguanas = 0
    serpientes = 0
    _listado = []
    
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorEscamas = None, largoCola = False ) :
        
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    @classmethod
    def setListado(cls, listado):
        
        cls._listado = listado 
    
    @classmethod
    def getListado(cls):
        
        return cls._listado
    @classmethod
    def cantidadReptiles(cls):
        
        return len(Reptil._listado)
    
    def setColorEscamas(self, colorEscamas):
        
        self._colorEscamas = colorEscamas
        
    def getColorEscamas(self):
        
        return self._colorEscamas
    
    def setLargoCola(self, largoCola):
        
        self._largoCola = largoCola
        
    def getLargoCola(self):
        
        return self._largoCola
    @staticmethod
    def movimiento():
        
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        
        nuevaIguana = Reptil(nombre, edad, "selva", genero, "rojo", True )
        Reptil.iguanas+=1
        return nuevaIguana
        
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        
        nuevaSerpiente = Reptil(nombre, edad, "selva", genero, "negro y amarillo", False)
        Reptil.serpientes+=1
        return nuevaSerpiente
    