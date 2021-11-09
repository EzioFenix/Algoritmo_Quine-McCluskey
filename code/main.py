import tabla
import tablero
from os.path import exists
import sys

def leerArchivo()->list:
    if exists('input.txt'):
        print('Archivo input.txt encontrado =D\n')
    with open('input.txt') as f:
        aux=f.readline()
    aux=aux.split(',')
    aux2=[]
    for i in aux:
        aux2.append(int(i))
    return aux2.copy()

def pedirVariables()->int:
    print('Ingresa el número de variables')
    numVariables=int(input('-'))
    return numVariables

def pedirMiniterminos()->list:
    """Obtiene los valores de los miniterminos y el numero de variables utilizadas

    Returns:
        list: [numVariables,minitermino1,mini2,...,minitermino-n]
    """
    print('Ingresa el número de miniterminos, por ejemplo 1, intro 2, intro 5, ingresa t para terminar de ingresar')
    aux='f'
    aux2=[]
    aux.append(numVariables)
    while aux!='t':
        aux=input('-')
        if aux!='t':
            aux2.append(int(aux))
    return aux2.copy()

def pedirDontCare()->int:
    """Pregunta al usuario si existen terminos don´t care 

    Returns:
        int: [description]
    """
    print('¿Tiene miniterminots don´t care? s=si, n=no')
    aux=input('-')
    if aux=='s' or aux=='S':
        print('De los miniterminos ingresados, cual es el primer termino don´t care que aparece de izquierda a derecha')
        aux2=input('-')
        print('Entendido, don´t care introducido')
        return int(aux2)
    else:
        return -1


def main():

    miniterminos=int()
    numVariables=int()
    indiceDontCare=int()
    if  exists('input.txt'):
        aux=leerArchivo()
        numVariables=aux.pop(0)
        indiceDontCare=aux.pop(-1)
        miniterminos=aux.copy()
    else:
        numVariables=pedirVariables()
        indiceDontCare=pedirDontCare()
        miniterminos=pedirMiniterminos()
    
    original_stdout = sys.stdout # Save a reference to the original standard output

    with open('output.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.


        

        # Crear tabla de minimizacion
        
        table=tabla.tabla(miniterminos, numVariables)
        
        #print('Miniterminos iniciales:')
        #table.imprimir2()
        while 0<len(table.renglones):
            table.ordenarRenglon()
        table.eliminarRepetidos()
        print('Tabla de minimizaciones')
        table.imprimir()



        
        tablerro=tablero.Tablero(miniterminos, table.oldRenglones,indiceDontCare)
        tablerro.minimizar()

        print('\n Miniterminos Resultado')
        tablerro.imprimir()
        sys.stdout = original_stdout # Reset the standard output to its original value
    print('archivo output.txt generado')
    

if __name__ == '__main__':
    main()
    """ if
    test=True
    if test==True:
        unittest.main()
    else:
        numVariables,miniterminos=pantallaInicio()
        programa(miniterminos, numVariables) """