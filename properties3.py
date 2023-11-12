#Acceder a los atributos via property

class Student:
    def __init__(self,name,code,note):
        self._name = name
        self.code = code
        self.note = note
    
    #Definir los metodos de acceso a los atributos   
    def get_name(self):
        print('Name accesing')
        return self._name
    def set_name(self,name):
        print('name was modified')
        self._name = name
    def del_name(self):
        print('name was deleted')
        del self._name
    
    #Implementar los metodos usando property
    name = property(get_name,set_name,del_name)

student = Student('Laura','064064','5.0')
student.name = 'Jassells'
print(student.name)



