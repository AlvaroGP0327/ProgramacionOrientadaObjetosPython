'''Se manejan tres tipos de atributos en python
atributos de instancia (normales, particulares de cada objeto),
atributos de clase (afuera de metodos, se heredan, son globales),
atributos de datos(se asignan despues de instanciar,validos solo en un objeto)'''

class Vehicle():
    impuesto_general = 2500 # Atributo de clase 

    def __init__(self, brand, year): #Atributos de instancia
        self.brand = brand
        self.year = year

    def power_on(self):
        return 'Encendiendo el motor'
    
    def power_off(self):
        return 'Apagando el motor'

class Car(Vehicle):
    def __init__(self, brand, year, wheels):
        self.wheels = wheels
        super().__init__(brand, year)    

class Motorcycle(Vehicle):
    def __init__(self, brand, year,wheel):
        self.wheel = wheel
        super().__init__(brand, year)

car = Car('Mazda', 2022, '4wheels')
moto = Motorcycle('Honda', 1988, '2wheels' )
#Vehicle.impuesto_general = 'nuevo_cargo de impuestos'
print('AUTOMOVIL')
print(car.brand)
print(car.year)
print(car.wheels)
#Implementacion atributo de dato
car.impuesto_general =  'Impuesto solo para carros'
print(car.impuesto_general)
car.adornos = 'Calcomanias' # Atributo no definido en ninguna clase padre.creado en la instancia
print(car.adornos)
print()
print('MOTOCICLETA')
print(moto.brand)
print(moto.year)
print(moto.wheel)
#Implementacion del atributo de clase
print(f"Impuesto al automotor: {moto.impuesto_general}")
 

