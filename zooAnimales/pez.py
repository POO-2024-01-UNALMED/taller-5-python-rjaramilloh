from animal import Animal
class Pez (Animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorEscamas=None, cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def cantidadPeces():
        return len(Pez.listado)
    
    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        pez = Pez(nombre,edad,"oceano",genero,"rojo",6)
        Pez.salmones+=1
        return pez
    
    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        pez = Pez(nombre,edad,"oceano",genero,"gris",6)
        Pez.bacalaos+=1
        return pez
    
    def setColorEscamas (self, colorEscamas):
        self._colorEscamas=colorEscamas

    def getColorEscamas (self):
        return self._colorEscamas
    
    def setCantidadAletas (self, cantidadAletas):
        self._cantidadAletas=cantidadAletas

    def getCantidadAletas (self):
        return self._cantidadAletas

    @classmethod
    def setListado(cls, listado):
        cls._listado=listado
    
    @classmethod
    def getListado(cls):
        return cls._listado