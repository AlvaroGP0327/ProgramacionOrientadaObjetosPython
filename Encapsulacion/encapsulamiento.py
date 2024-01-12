#Encapsular los atributos privados (__atributo) usando metodos para acceder a ellos
#Privacidad del atributo consiste en si accedido o no desde fuera de la clase
#Encapsulamiento sin el uso de decoradores
class User():

    def __init__(self, nombre, apellido, correo, contrasena, telefono) -> None:
       #Atributos publicos 
        self.nombre= nombre
        self.apellido= apellido
        self.correo= correo
        self.contrasena = contrasena
        #Atributos privados
        self.__telefono = telefono

    def get_telefono(self):
        #permite implementar una logica extra antes de leer un atributo
        return self.__telefono

    def set_telefono(self, nuevo_telefono):
        #permite implementar una logixa extra antes de escribir sobre un atributo
        self.__telefono = nuevo_telefono  
    
    def encriptar_contrasena(self, contrasena):
        pass

    def verificar_contrasena(self,contrasena):
        pass

usuario1 = User(nombre="Miryam", apellido="Pretel", correo="samiza16@gmail.com",
                 contrasena="0420,", telefono= "+573176624233")


print(usuario1.nombre)
#print(usuario1.__telefono) #No es posible acceder a un atributo privado de esta forma
print(usuario1.get_telefono())
#usuario1.__telefono = "00000000" #No es posible de esta forma modificar el atributo
usuario1.set_telefono(+573166684233) #Intermediario el metodo set_() si se puede cambiar el atributo
print(usuario1.get_telefono())




