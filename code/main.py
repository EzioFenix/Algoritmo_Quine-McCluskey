import tabla
import tablero
from os.path import exists

    
def pedirNumero()->list:
    """Obtiene los valores de los miniterminos y el numero de variables utilizadas

    Returns:
        list: [numVariables,minitermino1,mini2,...,minitermino-n]
    """
    if exists('input.txt'):
        print('Archivo input.txt encontrado')
        with open('input.txt') as f:
            aux=f.readline()
        aux=aux.split(',')
        aux2=[]
        for i in aux:
            aux2.append(int(i))
        return aux2
    else:
        print('Ingresa el número de variables')
        numVariables=int(input(''))
        print('Ingresa el número de miniterminos, por ejemplo 1, intro 2, intro 5, ingresa t para terminar de ingresar')
        aux='f'
        aux2=[]
        aux.append(numVariables)
        while aux!='t':
            aux=input('-')
            if aux!='t':
                aux2.append(int(aux))
        return aux2


def main():
    miniterminos=pedirNumero()
    numVariables=miniterminos.pop(0)

    # Crear tabla de minimizacion
    table=tabla.tabla(miniterminos, numVariables)
    
    table.imprimir2()
    while 0<len(table.renglones):
        table.ordenarRenglon()
    #print(len(table.renglones))
    table.eliminarRepetidos()
    #table.imprimir()

    tablerro=tablero.Tablero(miniterminos, table.oldRenglones)
    tablerro.minimizar()
    tablerro.imprimir()
    

if __name__ == '__main__':
    main()
    """ if
    test=True
    if test==True:
        unittest.main()
    else:
        numVariables,miniterminos=pantallaInicio()
        programa(miniterminos, numVariables) """