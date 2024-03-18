class Zona:

    def __init__ (self, nombre = None, zoo = None, animales = []):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales

    def agregarAnimales (self, animales):
        self._animales.append(animales)

    def cantidadAnimales (self):
        cantidaAnimales = len(self._animales)
        return cantidaAnimales
    
    def setNombre(self,nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre
    
    def setZoo(self, zoo):
        self._zoo = zoo
    
    def getZoo(self):
        return self._zoo
    
    def setAnimales(self, animales):
        self._animales = animales

    def getAnimales(self):
        return self._animales