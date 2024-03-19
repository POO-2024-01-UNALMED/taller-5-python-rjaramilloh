from zooAnimales.animal import Animal
class Mamifero(Animal):
    
    caballos = 0
    leones = 0
    _listado = []
    
    def __init__(self, nombre = None , edad = 0 , habitat = None , genero = None , pelaje = False , patas = 0 ) :
        
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def setListado(cls, listado):
        
        cls._listado = listado 
    
    @classmethod
    def getListado(cls):
        
        return cls._listado
    @classmethod
    def cantidadMamiferos(cls):
        
        return len(Mamifero._listado)
    
    def setPelaje(self, pelaje):
        
        self._pelaje = pelaje
        
    def isPelaje(self):
        
        return self._pelaje
        
    def setPatas(self, patas):
        
        self._patas = patas
        
    def getPatas(self):
        
        return self._patas
    
    @classmethod
    def crearCaballo(cls, nombre, edad , genero ):
        
        nuevoCaballo = Mamifero(nombre, edad, "pradera", genero, True, 4 )
        Mamifero.caballos+=1
        return nuevoCaballo
        
    @classmethod
    def crearLeon(cls, nombre = None, edad = 0, genero = None):
        
        nuevoLeon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones+=1
        return nuevoLeon
    