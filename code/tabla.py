import renglon
class tabla():
    def __init__(self,miniterminos,numVariables):
        self.numVariables=numVariables
        self.indices=[]
        self.oldRenglones=[]
        self.renglones:renglon=[]
        for mini in miniterminos:
            aux=renglon.renglon(mini,0,None,[])
            aux=renglon.renglon(mini)
            aux.primeraGeneracion(numVariables)
            self.renglones.append(aux)


    def eliminarRepetidos(self):
        i=0
        while i<len(self.oldRenglones)-1:
            if self.oldRenglones[i]== self.oldRenglones[i+1]:
                self.oldRenglones.pop(i)
            else:
                i=i+1

            

    def imprimir(self):
        texto="{:<3}| {:<2} | {:<16} \t| {:<30} \t|".format("generacion",'indice','bits','miniterminos')
        for mini in self.oldRenglones:
            print(mini)

    def imprimir2(self):
        texto="{:<10} \t| {:<10} \t| {:<10} \t| {:<30} \t|".format("generacion",'indice','bits','miniterminos')
        for mini in self.renglones:
            print(mini)



    def minimizacion(self,grupos:list):
        """Minimizan los renglones a partir de los viejos renglones

        Args:
            grupos (list): Lista de renglones divididos gracias a su numeros de indice
        """
        nuevosRenglones=[]
        for i in range(0,len(grupos)-1):
            for x in grupos[i]:
                for y in grupos[i+1]:
                    # si las diferencias son iguales o menores a 1
                    if x-y<=1:
                        # Se simplifica los dor miniterminos a 1 solo
                        nuevosRenglones.append(x+y)
                        # Se marca como que tuvieron decendencia
                        x.Continua()
                        y.Continua()
        # Se mueven los renglones a los viejos renglones
        self.oldRenglones=self.oldRenglones + self.renglones
        self.renglones=nuevosRenglones


    
    def ordenarRenglon(self):
        """Divide los renglones por número de 1's que contenta en su indice,

        Al final llama a la función de minimización

        Ejemplo 1100 => indice=2 => aux[2]=1110
        """
        aux=[]
        # Las divisiones en el eje Y, 1 por cada 1 que puede en los numeros de bits
        # ejemplo 1111 => max 4 bits
        for i in range(self.numVariables+1):
            aux.append([])


        # Dividir por numero de 1's    
        for mini in self.renglones:
            aux[mini.indice].append(mini)
        
        self.minimizacion(aux)
