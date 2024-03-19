class Zoologico:
    
    _zonas = []

    def __init__ (self, nombre = None, ubicacion = None) :
        
        self._nombre = nombre
        self._ubicacion = ubicacion

    def setNombre (self, nombre):
        
        self._nombre = nombre

    def getNombre(self):
        
        return self._nombre
    
    def setUbicacion(self, ubicacion):
        
        self._ubicacion = ubicacion
        
    def getUbicacion(self):
        
        return self._ubicacion
    @classmethod
    def setZona(cls, zonas):
        
        cls._zonas = zonas
    @classmethod
    def getZona(cls):
        
        return cls._zonas
    @classmethod
    def agregarZonas(cls, zona):
        
        cls._zonas.append(zona)
    @classmethod   
    def cantidadTotalAnimales(cls):
        
        cantAnimales = 0
        
        for zona in cls._zonas:
            
            cantAnimales += zona.cantidadAnimales()
        
        return cantAnimales