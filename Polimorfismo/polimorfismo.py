#Cree una clase Figura con los atributos x, y height,widht
# Ver el archivo de Herencia.py donde esta mejor implementado el ejemplo
class Shape():
    def __init__(self, x, y, height, width) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.x = width

    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, radius) -> None:
        self.radius = radius
        super().__init__(x, y,)

        
