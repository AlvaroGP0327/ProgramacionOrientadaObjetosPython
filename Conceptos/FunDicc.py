#Un diccionario puede tomar como valores
#funciones las cuales pueden ser llamadas
#usando las claves asociadas a cada funcion

from time import sleep
def menu_selector():
    opciones = {'1':dias,'2':tardes,'3':noches, '4':salir}
    opcion = None
    while opcion !='4' :
        print('1-manana') 
        print('2-tarde')
        print('3-noche')
        print('4-SALIR')
    
        try:
            opcion = input('SELECCIONE UNA OPCION')
            sleep(2)
            seleccion = opciones[opcion] # El diccionarion me esta retornando una funcion
            seleccion() #Llamada a la funcion que me retorna el diccionario
        except KeyError:
            print("Opcion Invalida")

def dias():
    print('BUEN DIA')

def tardes():
    print('BUENA TARDE')

def noches():
    print('BUENA NOCHE')

def salir():
    print('MENU CERRADO')

menu_selector()
