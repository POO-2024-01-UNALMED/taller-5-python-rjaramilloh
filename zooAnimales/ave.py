from animal import Animal
class Ave (Animal):

    _listado = []
    halcones = 0
    agulas = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def cantidadAves():
        return len(Ave.listado)
    
    def movimiento(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        ave = Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        Ave.halcones+=1
        return ave
    
    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        ave = Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        Ave.agulas+=1
        return ave
    
    def setColorPlumas (self, colorPlumas):
        self._colorPlumas= colorPlumas

    def getColorPlumas (self):
        return self._colorPlumas
    
    @classmethod
    def setListado(cls, listado):
        cls._listado=listado
    
    @classmethod
    def getListado(cls):
        return cls._listado