class Escuderia:
    def __init__(self):
        self.__nombre=None
        self.__motor= None
        self.__piloto1=None
        self.__piloto2=None
        self.__costoAnual= None
    
    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato

    @property 
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, dato):
        self.__motor = dato

    @property 
    def piloto1(self):
        return self.__piloto1
    
    @piloto1.setter
    def piloto1(self, dato):
        self.__piloto1 = dato

    @property 
    def piloto2(self):
        return self.__piloto2
    
    @piloto2.setter
    def piloto2(self, dato):
        self.__piloto2 = dato
        
    @property 
    def costoAnual(self):
        return self.__costoAnual
    
    @costoAnual.setter
    def costoAnual(self, dato):
        self.__costoAnual = dato