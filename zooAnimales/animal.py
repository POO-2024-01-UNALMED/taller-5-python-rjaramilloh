from  gestion.zona import Zona
from mamifero import Mamifero
from ave import Ave
from reptil import Reptil
from pez import Pez
from anfibio import Anfibio

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
    
    def totalPorTipo(cls):
        return "Mamiferos:"+len(Mamifero.getListado())+"\n"+"Aves:"+len(Ave.getListado())+"\n"+"Reptiles:"+len(Reptil.getListado())+"\n"+"Peces:"+len(Pez.getListado())+"\n"+"Anfibios:"+len(Anfibio.getListado())

    def __str__(self):
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