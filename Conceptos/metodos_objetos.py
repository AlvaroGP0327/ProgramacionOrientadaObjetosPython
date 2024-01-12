class Auto():
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
    
    def acelerar(self, masvelocidad):
        self.velocidad = masvelocidad

    @classmethod
    def frenar(cls,menosvelocidad):
        #No espera una instancia para implementarse
        print('disminuyendo la velocidad') 

auto = Auto('Nissan350z', 2018)
auto.acelerar(500)
#Llamado a un metodo de clase desde la instancia
auto.frenar(100) 
Auto.frenar(100) 
#Llamado a una funcion de clase/ no requiere de instancia
        