#Encapsular los atributos privados (_atributo) usando metodos para acceder a ellos
#Privacidad del atributo consiste en si accedido o no desde fuera de la clase
#Encapsulamiento sin el uso de decoradores.
#_atributo el guion bajo que se pone antes de la definicion
#del nombre del atributo es una CONVENCION en lugar de una implementacion
#como en otros lenguajes. La CONVENCION le indica al desarrollador que NO
#debe acceder al atributo directamente, en su lugar debe acceder al atributo
#via sus metodos.

class User():

    def __init__(self, nombre, apellido, correo, contrasena, telefono) -> None:
       #Atributos publicos 
        self.nombre= nombre
        self.apellido= apellido
        self.correo= correo
        self.contrasena = contrasena
        #Atributos privados
        self._telefono = telefono

    def get_telefono(self):
        #permite implementar una logica extra antes de leer un atributo
        return self._telefono

    def set_telefono(self, nuevo_telefono):
        #permite implementar una logica extra antes de escribir sobre un atributo
        self._telefono = nuevo_telefono  
    
    def encriptar_contrasena(self, contrasena):
        pass

    def verificar_contrasena(self,contrasena):
        pass

usuario1 = User(nombre="Miryam", apellido="Pretel", correo="samiza16@gmail.com",
                 contrasena="0420,", telefono= "+573176624233")


print(usuario1.nombre)
print(usuario1.get_telefono())
usuario1.set_telefono(+573166684233) #Intermediario el metodo set_() si se puede cambiar el atributo
print(usuario1.get_telefono())




