#Encapsular el atributo precio
#EXCELENTE y funcional implementacion
#de la encapsulacion de atributos
class Productos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio # Atributo privado

    @property
    #Getter
    def precio(self): #Ponerle al metodo el nombre del atributo que quiero encapsular
        print('Accediendo al precio')
        return self._precio
    #Setter
    @precio.setter
    def precio(self,precio):
        print('Cambiando de precio....')        
        if precio > 0:
            self._precio = float(precio)
        else:
            print('Valor de precio incorrecto, no se puede cambiar')

#Funciona
producto = Productos(nombre='Arroz', precio= 12.46)
producto.precio = -40.00
print(producto.precio)


    
