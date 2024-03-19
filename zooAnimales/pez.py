from zooAnimales.animal import Animal
class Pez(Animal):
    
    salmones = 0
    bacalaos = 0
    _listado = []
    
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorEscamas = None, cantidadAletas = 0 ) :
        
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def setListado(cls, listado):
        
        cls._listado = listado 
    
    @classmethod
    def getListado(cls):
        
        return cls._listado
    @classmethod
    def cantidadPeces(cls):
        
        return len(Pez._listado)
    
    def setColorPiel(self, colorEscamas):
        
        self._colorEscamas = colorEscamas
        
    def getColorEscamas(self):
        
        return self._colorEscamas
    
    def setcantidadAletas(self, cantidadAletas):
        
        self._cantidadAletas = cantidadAletas
        
    def getCantidadAletas(self):
        
        return self._cantidadAletas
    
    @staticmethod
    def movimiento():
        
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        
        nuevoSalmon = Pez(nombre, edad, "selva", genero, "rojo", True )
        Pez.salmones+=1
        return nuevoSalmon
        
    @classmethod
    def crearBacalao(cls,nombre, edad, genero):
        
        nuevoBacalao = Pez(nombre, edad, "selva", genero, "negro y amarillo", False)
        Pez.bacalaos+=1
        return nuevoBacalao
    