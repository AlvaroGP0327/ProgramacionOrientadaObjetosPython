'''Definicin de una clase base abstracta
Se usa para heredar metodos que deben ser
implementados por las clases hijas.
No se pueden instanciar directamemte
'''
from abc import ABC, abstractmethod, abstractproperty

class Persona(ABC):

    @abstractproperty
    def ciudad():
        pass
    
    @abstractproperty
    def identificacion():
        pass

    @abstractmethod
    def reir(self):
        pass
    
    def caminar(self):
        print("Me gusta caminar en las noches")

class Payaso(Persona):

    def __init__(self) -> None:
        super().__init__()    
        self._city = None
        self._numero_id = 0
    
    @property
    def identificacion(self):
        return "ID; Soy el payaso Pimpim"
    @identificacion.setter
    def identificacion(self,num_id):
        self._numero_id = num_id


    def etiqueta(self):
        return 'Hola soy un payaso'

    def reir(self):
        return "Me rio como un payaso"

#El metodo abstracto ciudad sera el mediador para el atributo city    
    @property
    def ciudad(self):
        return self._city
    
    @ciudad.setter
    def ciudad(self,cd):
        print("asignando ciudad")
        self._city = cd

payaso = Payaso()
payaso.ciudad = "Boston"
print(payaso.ciudad)









