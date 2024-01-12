'''No es tan estricta como en Java
pero puede implementarse por medio
de una clase base abstracta y al herencia
Otra aproximacion es usando la anotacion
Protocol para versiones python 3.8+'''

from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def calcular_area():
        pass

    def decir_color(self):
        return "Soy una superficie color..."

class Triangulo(Interface):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base *self.altura)/2

    def decir_color(self):
        return "Sobreescribir el metodo decir_color"
    
triangulo =  Triangulo(5,5)
print(triangulo.decir_color())
print(triangulo.calcular_area())
        
