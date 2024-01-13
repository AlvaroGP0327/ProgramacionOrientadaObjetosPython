# @properties cuando lo vi en EDTeam

class User():
    def __init__(self, nombre, apellido, correo) -> None:
        self._nombre= nombre
        self.apellido= apellido
        self._correo= correo

    # Getters 
    @property
    def nombre(self):
        print('Mostrando nombre')
        return self._nombre
    
    #Setters
    @nombre.setter
    def nombre(self, nuevo_nombre):
        print('Actualizando nombre')
        self._nombre = nuevo_nombre

    #Encapsulando el atributo correo
    @property
    #Getter
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo
        return 'Correo modificado'
    

usuario = User('Laura', 'Gonzales', 'samiza@gmail.com')
print(usuario)
print(usuario.nombre)
print(usuario.apellido)
print(usuario.correo)
    

