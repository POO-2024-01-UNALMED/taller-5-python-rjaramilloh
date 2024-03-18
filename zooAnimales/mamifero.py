from animal import Animal
class Mamifero (Animal):

    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, pelaje = False, patas = 0 ):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)

    def cantidadMamiferos():
        return len(Mamifero.listado)
    
    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        mamifero = Mamifero(nombre,edad,"pradera",genero,True,4)
        Mamifero.caballos+=1
        return mamifero
    
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        mamifero = Mamifero(nombre,edad,"selva",genero,True,4)
        Mamifero.leones+=1
        return mamifero
    
    def setPelaje(self, pelaje):
        self._pelaje=pelaje
    
    def getPelaje(self):
        return self._pelaje
    
    def setPatas(self, patas):
        self._patas=patas
    
    def getPatas(self):
        return self._patas
    
    @classmethod
    def setListado(cls, listado):
        cls._listado=listado
    
    @classmethod
    def getListado(cls):
        return cls._listado