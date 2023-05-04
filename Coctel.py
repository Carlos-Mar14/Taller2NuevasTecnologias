class Coctel:
    def __init__(self):
        self.__nombre=None
        self.__precio=None
        self.__cantidad=None
        self.__grados=None
        self.__tipoCoctel=None
        self.__anejamiento=None
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, dato):
        self.__nombre=dato
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, dato):
        self.precio=dato
        
    @property
    def cantidad(self):
        return self.__cantidad
    
    @nombre.setter
    def cantidad(self, dato):
        self.__cantidad=dato
    
    @property
    def grados(self):
        return self.__grados
    
    @grados.setter
    def nombre(self, dato):
        self.__grados=dato
        
    @property
    def tipoCoctel(self):
        return self.__tipoCoctel
    
    @grados.setter
    def tipoCoctel(self, dato):
        self.__tipoCoctel=dato
        
    @property
    def anejamiento(self):
        return self.__anejamiento
    
    @nombre.setter
    def anejamiento(self, dato):
        self.__anejamiento=dato
        
        