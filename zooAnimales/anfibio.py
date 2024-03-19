from zooAnimales.animal import Animal
class Anfibio(Animal):
    
    ranas = 0
    salamandras = 0
    _listado = []
    
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorPiel = None, venenoso = False ) :
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def setListado(cls, listado):
        
        cls._listado = listado 
    
    @classmethod
    def getListado(cls):
        
        return cls._listado
    
    @classmethod
    def cantidadAnfibios(cls):
        
        return len(Anfibio._listado)
    
    def setColorPiel(self, colorPiel):
        
        self._colorPiel = colorPiel
        
    def getColorPiel(self):
        
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        
        self._venenoso = venenoso
        
    def isVenenoso(self):
        
        return self._venenoso
    
    @staticmethod
    def movimiento():
        
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        
        nuevaRana = Anfibio(nombre, edad, "selva", genero, "rojo", True )
        Anfibio.ranas+=1
        return nuevaRana
        
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        
        nuevaSalamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras+=1
        return nuevaSalamandra
    