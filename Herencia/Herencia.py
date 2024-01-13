# Crear una clase de vehiculos
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    @abstractmethod
    def road_trip(self):
        pass

# Clase hija
class Car(Vehicle):
    def __init__(self, brand, year, wheels):
        self.wheels = wheels
        super().__init__(brand, year) 

    def road_trip(self):
        print('Rodando por el camino...')


class Boat(Vehicle):
    def __init__(self, brand, year, hydrodinamics):
        self.hydrodinamics = hydrodinamics
        super().__init__(brand, year)

    def road_trip(self):
        print('Navegando sobre el agua...')

class Plane(Vehicle):
    def __init__(self, brand, year, flying):
        self.flying = flying
        super().__init__(brand, year)

    def road_trip(self):
        print('Despegar y volar...')

# Crear instanciar cada una de las clases

car = Car(brand='Nissan', year= 2022, wheels='four wheels')
boat = Boat(brand='Yate', year= 2023, hydrodinamics='fullSpeed')
plane = Plane(brand='Boeing',year= 1995, flying='WingsUp')
print(car)
print(boat)
print(plane)
'''Algo basico sobre polimorfismo mismo metodo heredado,
pero implementado de distinta forma en cada objeto'''
car.road_trip()
boat.road_trip()
plane.road_trip()

