'''Decoradores:
 @staticmethod @classmethod'''

class Pintar():
    #Atributos de instancia
    def __init__(self, color) -> None:
        self.color = color
#Atributo de clase
#Pertenece a la clase y a todas sus instancias
    superficie = 'Pared'    
    
    @classmethod
    def metodo_clase(cls):
        #Se implementa para acceder a los atributos de clase
        #toda modificacion en la clase afecta a todas las 
        #instancias
        #Se llama desde la clase
        #No puede acceder a los atributos de instancia
        #Para acceder a los atributos de la instancia
        #se le debe pasar al metodo de clase la instancia
        #como parametro
        print('Este es un metodo de clase...')
        print('Desde aqui modificar la superficie') 
   
    @staticmethod
    def metodo_estatico():
        #Es una funcion que depende siempre de la clase, no se implementa en las instancias
        # No tiene acceso a los atributos ni de la clase ni de la instancia
        #Se llama desde la clase
        #Se usa cuando quiero usar un metodo sin necesidad de instanciar un objeto
        print('Este es un metodo estatico...')

    def metodo_instancia(self):
        # El normal que se modifica en las instancias sin afectar a las otras ni a la clase
        # Se llama desde la instancia
        print('Este es un metodo de instancia...')

#Ejemplo @classmethod

class Figura():
    def __init__(self,color) -> None:
        self.color = color

    forma = "Tiangulo"
    
    #Se puede modificar un atributo de clase
    #desde un metodo de clase
    @classmethod
    def cambiar_forma(cls,nueva_forma):
        print('Implementar alguna logica')
        cls.forma = nueva_forma

figura1 = Figura('amarillo')
figura2 = Figura('azul')
figura3 = Figura('rojo')

print(figura1.forma)
print(figura1.color)
#Los cambios en los atributos de clase
#que se hagan por asignacion directa al atributo
#de clase o mediante el @classmethod se veran
#reflejados en todas las instancias.
Figura.cambiar_forma("Cuadrado")
print(figura1.forma)
print(figura1.color)
print(figura2.color)
print(figura2.forma)
print(Pintar.metodo_estatico())
figura3.forma = 'Paralelepipedo'
print(figura3.forma)
print(figura1.forma)






    


