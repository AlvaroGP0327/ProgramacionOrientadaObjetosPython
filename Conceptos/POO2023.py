#Cursos POO en Python 2023/EDTeam

#Defina una clase con atributos(nombre,apellido,correo,pass,telefono)
#Usar el metodo constructor para definir propiedades iniciales de los objetos a instanciar
#Es posible pasar una funcion como parametro para una clase,
#Asi las instancias van a poder usar la funcion.
def saludar(jornada):
    print(f"you will charge in {jornada}")

class User():
    # Datos (atributos)
    def __init__(self, nombre, apellido, correo, contrasena, telefono,saludar) -> None:
        '''El self al principio indica que el atributo puede ser accedido por
        todos los elementos (metodos y atributos) que conforman la'''
        self.nombre= nombre
        self.apellido= apellido
        self.correo= correo
        self.contrasena= contrasena
        self.telefono= telefono
        self.saludar = saludar
# Funcionalidades (Metodos) 
# Deben recibir siempre el argumento self
    def verificar_contrasena(self):
        pass
    def encriptar_contrasena(self): 
        pass

#Haga una instancia de la clase
#Al construir la instancia no se pasan parametros a la funcion/atributo
#Esto se hace porque lo que quiero es tener disponible la funcion
#Pero no llamarla
#Tambien es posible pasar como parametro otra clase
#Esto es util para que interactuen los metodos de ambos objetos
#Uno con el otro al ser instanciados

user1 = User(nombre='Alvaro', apellido='Gamboa', 
             correo='customerm552@gmail.com', 
             contrasena='laloylala0420', telefono= '2677484473',
             saludar=saludar
             )
user2 = User(nombre='Laura', apellido='Gonzales', 
             correo='samiza_16@gmail.com', 
             contrasena='lamuerdo', telefono= '2676998665',
             saludar=saludar)

user1.saludar("morning")
user2.saludar("night")

 




