from animal import Animal
class Reptil (Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorEscamas=None, largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def cantidadReptiles():
        return len(Reptil.listado)
    
    def movimiento(self):
        return "reptar"
    
    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        reptil = Reptil(nombre,edad,"humedal",genero,"verde",3)
        Reptil.iguanas+=1
        return reptil
    
    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        reptil = Reptil(nombre,edad,"jungla",genero,"blanco",1)
        Reptil.serpientes+=1
        return reptil
    
    def setColorEscamas (self, colorEscamas):
        self._colorEscamas=colorEscamas

    def getColorEscamas (self):
        return self._colorEscamas
    
    def setLargoCola (self, largoCola):
        self._largoCola=largoCola

    def getLargoCola (self):
        return self._largoCola

    @classmethod
    def setListado(cls, listado):
        cls._listado=listado
    
    @classmethod
    def getListado(cls):
        return cls._listado