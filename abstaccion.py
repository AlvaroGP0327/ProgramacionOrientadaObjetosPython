from cryptocode  import encrypt, decrypt
from abc import ABC, abstractmethod # Decorador para los metodos de clase

# Cree una clase usuario base con los atributos requeridos(NOM,AP,CORR,CON,TEL)
 
#Clase Base Abstracta que se usa para construir otras clases
class Users(ABC):
    def __init__(self, nombre, apellido, correo, contrasena, telefono) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        #Agregar la contrasena usando un metodo de clase
        self.contrasena = self.encrypt_pass(self, contrasena)
        self.telefono = telefono
    
    @abstractmethod 
    #Indica a las clases hijas que tienen que tener SI O SI el metodo
    #que engloba el metodo abstracto.
    def encrypt_pass(self, contrasena) -> str :
        pass
    @abstractmethod    
    def decrypt_pass(self, contraencrypt) -> str :
        pass

#Clase HIJA
class User1(Users):
    
    def encrypt_pass(self, contrasena) -> str:
        #Metodo "mediador" para escribir en el atributo contrasena
        #Y encriptar el dato antes de asignarlo al atributo
        return encrypt(contrasena, "secret")
    
    def decrypt_pass(self, contrasena) -> str:
        # Metodo para acceder al atributo contrasena
        # Y compararlo con un dato ingresado al llamar el metodo
        decrypt_pass = decrypt(self.contrasena, "secret")
        return decrypt_pass == contrasena
    
#Creando la instancia
UsuarioBanco = User1(nombre='Laura', apellido='Gonzales', correo='samyza16@gmail.com',
                    contrasena= '0420',telefono= '2676998665'
                    )
print(UsuarioBanco)
print(UsuarioBanco.contrasena) #Efectivamente guarda la contrasena encriptada
print(UsuarioBanco.decrypt_pass('lamuerdo')) #Devuelve False al ser el pass incorrecto
print(UsuarioBanco.decrypt_pass('0420')) #Devuelve True al ser el pass correcto



