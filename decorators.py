#Estudio desde el video ClearCode
#Understanding decorators

'''En general los decoradores son funciones
que envuelven a otras funciones'''
'''Se usan principalmente en tres
circunstancias:
1-Testear codigo sin cambiarlo
2-Trabajar en equipo y evitar cambios 
innecesarios en el codigo
3- Dentro de las clases permiten ejecutar
codigo antes de acceder a algun atributo.'''

def func1():
    print('Function 1 activated')

def wrapper(arg_function):
    #Funcion que recibe una funcion como argumento
    #Pero que tambien tiene su propia logica
    print('Start logic wrapper')
    arg_function()
    print('Ends logic wrapper')

def function_generator():
    #Al llamar a function generator crear y retornar una funcion
    print('Building a function...')
    def new_function():
        print('A new function was created')

    return new_function

'''implementando decoradores'''
'''
1- Se escribe la funcionalidad del decorador (wrapper)
2- Se llama el wrapper utilizando @
3- Dentro del decorador @ escribir la logica de la funcion '''
def decorator(func):
    print('decorator logic start')
    func()
    print('decorator logic ends')

@decorator
def func2():
    print('Function by decorator was implemented')

#new_function = function_generator()
#print(type(new_function))
#new_function()


