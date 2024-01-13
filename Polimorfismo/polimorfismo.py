#Cree una clase Figura con los atributos x, y height,widht
# Ver el archivo de Herencia.py donde esta mejor implementado el ejemplo
class Shape():
    def __init__(self, x, y, heigth, width) -> None:
        self.x = x
        self.y = y
        self.heigth = heigth
        self.width = width

    def draw(self):
        print('hola desde shape')

class Circle(Shape):
    def __init__(self,height,width, x, y, radius) -> None:
        self.radius = radius
        super().__init__(x,y,height,width)

    def draw(self):
        return "Reescribir el metodo draw"

circle = Circle(2,2,3,3,5)

