#  LLAMADO A UNA FUNCION DESDE UN DICCIONARIO

def menu_selector():
    opciones = {'1':dias,'2':tardes,'3':noches, '4':salir}
    opcion = None
    while opcion !='4' :
        print('1- BUEN DIA') 
        print('2- BUENA TARDE')
        print('3- BUENA NOCHE')
        print('4- SALIR')
    
        opcion = input('SELECCIONE UNA OPCION')
        seleccion = opciones[opcion] # El diccionarion me esta retornando una funcion
        seleccion() #Llamada a la funcion que me retorna el diccionario
        
def dias():
    print('BUEN DIA')

def tardes():
    print('BUENA TARDE')

def noches():
    print('BUENA NOCHE')

def salir():
    print('MENU CERRADO')

menu_selector()
