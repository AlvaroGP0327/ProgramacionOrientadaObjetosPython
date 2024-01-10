#Decoradores @staticmethod @classmethod

class Pintar():
    def __init__(self, color) -> None:
        self.color = color

    superficie = 'Pared'    
    
    @classmethod
    def metodo_clase(cls):
        #Tiene acceso a TODOS los componentes de la clase
        #Desde aqui modificar atributos de clase
        # Los cambios en atributos de clase se reflejan en la instancia
        #Se llama desde la clase
        #No puede acceder a los atributos de instancia
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

mi_pintura = Pintar('VERDE')


    


