import zooAnimales
class Animal:
    _totalAnimales = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales+=1

    def movimiento (self):
        return "desplazarse"
    
    @staticmethod
    def totalPorTipo():
        return "Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\nAves : " + str(zooAnimales.ave.Ave.cantidadAves()) + "\nReptiles : " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces : " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\nAnfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
    
    def toString(self):
        if Animal.getZona()!=None:
            return "Mi nombre es "+ Animal.getNombre()+", tengo una edad de " +Animal.getEdad()+ ", habito en "+Animal.getHabitat()+" y mi genero es "+Animal.getGenero()+", la zona en la que me ubico es "+Animal.getZona().getNombre()+", en el "+Animal.getZona().getZoo().getNombre()
        else:
            return "Mi nombre es "+ Animal.getNombre()+", tengo una edad de " +Animal.getEdad()+ ", habito en "+Animal.getHabitat()+" y mi genero es "+Animal.getGenero()
		
    def setNombre(self,nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre
    
    def setEdad(self,edad):
        self._edad = edad
    
    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat=habitat
    
    def getHabitat(self):
        return self._habitat
    
    def setGenero(self, genero):
        self._genero=genero

    def getGenero(self):
        return self._genero
    
    def setZona(self,zona):
        self._zona=zona
    
    def getZona(self):
        return self._zona
    
    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
