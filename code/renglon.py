class renglon ():
    def __init__(self,numeroMinitermino=0,generacion=0,bits='',minis=[]):
        self.generacion=generacion
        self.indice=0
        self.bits=bits
        self.continua=False
        self.miniterminosSimpli=minis.copy()
        self.minitermino=numeroMinitermino
        # Numero de minitermino en caso de que sea  la primera tabla generado

    
    def miniterminosStr(self)->str:
        aux=[str(i)  for i in self.miniterminosSimpli]
        aux=",".join(aux)
        return aux

    def __eq__(self, other):
        if (self.generacion ==other.generacion) and (self.miniterminosSimpli==other.miniterminosSimpli) and (self.bits==other.bits):
            return True
        else:
            return False

    def toStr(self):
        aux3=[str(x) for x in self.miniterminosSimpli]
        aux3=','.join(aux3)
        return "│{:<10} \t│ {:<10} \t│ {:<10} \t│ {:<30} \t│".format(self.generacion,self.indice,self.bits,aux3)

    def __repr__(self):
        aux3=[str(x) for x in self.miniterminosSimpli]
        aux3=','.join(aux3)
        return "│{:<10} \t│ {:<10} \t│ {:<10} \t│ {:<30} \t│".format(self.generacion,self.indice,self.bits,aux3)

    def primeraGeneracion(self,numVariables:int):
        """Método para inicializar a la primera generación de la tabla

        Args:
            numVariables (int): numero de variables utilizadas en el circuito
            Example ABCXY => 5 variables 
        """
        self.generacion=0
        self.miniterminosSimpli.append(self.minitermino)
        self.miniterminosToArreglo(numVariables)
        self.contarUnos()


    def nextGeneration(self):
        """Método para inicializar de la generación 2 en adelante
        """
        self.contarUnos()
        
    
    def contarUnos(self)->int:
        """Cuenta el número de 1's en el arreglo de self.bits

        Returns:
            int: Número de 1's en el arreglo
        """
        contador=0
        for i in self.bits:
            if i=='1':
                contador=contador+1
        self.indice=contador


    def miniterminosToArreglo(self,numBits:int):
        """Convierte el número de minitermino a 1's y 0's, los 0's a la izquierda dependen del numero de bits

        Examples:

            0,numBits=5 => 00000
            8,numBits=5 => 01000
        """
        aux=bin(self.minitermino)
        aux=aux[2:]

        restantes=numBits-len(aux)
        self.bits= restantes *'0' + aux
        
    
    def __sub__(self,other):
        """Cuenta el numero de diferencias entre dos arreglos de bits

            - regresa 1, cuando son adyacentes
            - regresa mas, cuando no son adyacentes
        """
        size=len(self.bits)
        aux=[]
        diferencias=0
        for i in range(0,size):
            if self.bits[i]!=other.bits[i]:
                diferencias=diferencias+1
                if diferencias>1:
                    return diferencias
        return 1


    def __add__(self,other):
        """
        Devuelve la cadena de bits de los dos adyancentes renglones 
        """
        size=len(self.bits)
        aux=[]
        diferencias=0

        for i in range(0,size):
            if self.bits[i]=='-' or other.bits[i]=='-':
                aux.append('-')
            elif self.bits[i]==other.bits[i]:
                aux.append(self.bits[i])
            else:
                aux.append('-')
        aux=''.join(aux)
        #mini.extend(self.miniterminosSimpli)
        #mini.extend(other.miniterminosSimpli)
        minis= sorted(self.miniterminosSimpli + other.miniterminosSimpli)
        nuevo=renglon(0,self.generacion +1,aux,minis)
        nuevo.nextGeneration()

        return nuevo

    def Continua(self):
        self.continua=True