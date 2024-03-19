from zooAnimales.animal import Animal
class Ave(Animal):
    
    halcones = 0
    aguilas = 0
    _listado = []
    
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorPlumas = None) :
        
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def setListado(cls, listado):
        
        cls._listado = listado 
    
    @classmethod
    def getListado(cls):
        
        return cls._listado
    
    @classmethod
    def cantidadAves(cls):
        
        return len(Ave._listado)
    
    def setColorPlumas(self, colorPlumas):
        
        self._colorPlumas = colorPlumas
        
    def getColorPlumas(self):
        
        return self._colorPlumas
    @staticmethod
    def movimiento():
        
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        
        nuevoHalcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones+=1
        return nuevoHalcon
        
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        
        nuevaAguila = Ave(nombre, edad, "montanas", genero, "negro y amarillo")
        Ave.aguilas+=1
        return nuevaAguila
    