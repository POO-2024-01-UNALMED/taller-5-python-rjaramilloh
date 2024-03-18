from animal import Animal
class Anfibio (Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorPiel=None, venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)
    
    @staticmethod
    def movimiento():
        return "saltar"
    
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        anfibio = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        Anfibio.ranas+=1
        return anfibio
    
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        anfibio = Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        Anfibio.salamandras+=1
        return anfibio
    
    def setColorPiel (self, colorPiel):
        self._colorPiel=colorPiel

    def getColorPiel (self):
        return self._colorPiel
    
    def setVenenoso (self, venenoso):
        self._venenoso=venenoso

    def getVenenoso (self):
        return self._venenoso

    @classmethod
    def setListado(cls, listado):
        cls._listado=listado
    
    @classmethod
    def getListado(cls):
        return cls._listado