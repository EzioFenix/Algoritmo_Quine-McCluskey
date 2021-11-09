import renglon
class Tablero():

    def __init__(self,miniterminos:list,oldRenglones:list):
        self.renglonesHoja=[]
        self.renglonesResultado=[]
        self.miniterminos=miniterminos
        self.indices={}
        self.columnas=[]
        self.obtenerHojas(oldRenglones)
    

    def imprimir(self):
        for i in self.renglonesResultado:
            print(i)
    
    def minimizar(self):
        self.crearIndice()
        self.build()
        self.llenarTablero()
        self.seleccionarMiniterminos()


    def crearIndice(self):
        """Crea un diccionario que el número introducido con el número de indice correspondiente

        ejemplo de miniterminos y sus indices

        1=> 0
        3=> 1
        7=> 2
        8=> 3

        entre estos no hay espacios


        Args:
            miniterminos (): [list(int)]
        """
        indices={}
        numMiniterminos=len(self.miniterminos)
        for i in range(0,numMiniterminos):
            indices[self.miniterminos[i]]=i
        self.indices=indices.copy()


    def obtenerHojas(self,oldRenglones:list):
        """Obtenemos aquellos miniterminos que no se minimizarón con otros

        Las ramas obtenidas se le asignan a renglones
        """
        for renglon in reversed(oldRenglones):
            if renglon.continua==False:
                self.renglonesHoja.append(renglon)


    def build(self):
        """Contruye  el tablero de Y por X dimensiones con 0 todos

        El resultado se le asigna a self.columna
        """
        # Columna[Y][X] construimos el tablero
        columnas=[]
        y=len(self.renglonesHoja)
        x=len(self.indices)
        for y0 in range(0,y):
            columnas.append([])
            for x0 in range(0,x):
                columnas[y0].append(0)
        self.columnas=columnas.copy()
        print(self.columnas)


    def llenarTablero(self):
        """Introduce los datos de self.renglones[x].miniterminos en las columnas asignando 1's en donde exista un 1
        """
        y=0 
        for miniterminos in  self.renglonesHoja:
            for mini in miniterminos.miniterminosSimpli:
                x=self.indices[mini]
                self.columnas[y][x]=1
            y=y+1


    def apagar1s(self,arreglo,arreglo2,todas=False)->list:
        """Regresa arreglo - arreglo2

        Ejemplo:

        1010 - 1000 =>0010

        Pero regresa none si se quiere restar 1 en una posición que no tiene

        10 - 01 => 10

        Returns:
            [type]: [description]
        """
        nuevo=[]
        size=len(arreglo)
        if todas:
            for i in range(size):
                nuevo.append(0)
        else:
            for i in range(size):
                if (arreglo[i]>=1 and arreglo2[i]>=1) or (arreglo[i]==0 and arreglo2[i]==0):
                    nuevo.append(0)
                elif arreglo[i]>=1 and arreglo2[i]==0 or (arreglo[i]==0 and arreglo2[i]>=1):
                    nuevo.append(1)
        return nuevo


    def seleccionarMiniterminos(self):
        """Selecciona a los miniterminos que conforman la minimización total
        """
        renglonesResultantes=[]
        y=len(self.renglonesHoja)
        x=len(self.indices)

        print("{}x{}".format(str(y),str(x)))
        #En el arreglo unicos, donde tenga un 1 es aquel que sólo hay un minitermino que lo contiene
        #suma los 1's por columnas
        unicos=[]
        for x0 in range(x):
            unicos.append(0)
            for y0 in range(y):
                unicos[x0]=unicos[x0]+self.columnas[y0][x0]

        # Despues de haber sumado obtenemos los renglones que aportan un minitermino único
        numTermino:renglon=[]
        for x0 in range(0,x):
            y0=0
            if unicos[x0]==1:
                while y0<len(self.columnas):
                    # Buscamos el renglon que tenga el minitemino
                    if self.columnas[y0][x0]==1:
                        nuevo=self.renglonesHoja.pop(y0)
                        renglonesResultantes.append(nuevo)
                        unicos= self.apagar1s(unicos, self.columnas[y0])
                        self.columnas.pop(y0)
                        break
                    y0=y0+1

        
        # Obtener los terminos no unicos-----------------------

        # Ponemos a 1 todos los terminos no 0 de unicos
        for i in range(len(unicos)):
            if unicos[i]>0:
                unicos[i]=1


        # Cambiar esta parte por un algoritmo greedy después
        numTermino:renglon=[]
        for x0 in range(0,x):
            y0=0
            if unicos[x0]==1:
                while y0<len(self.columnas):
                    # Buscamos el renglon que tenga el minitemino
                    if self.columnas[y0][x0]==1:
                        nuevo=self.renglonesHoja.pop(y0)
                        renglonesResultantes.append(nuevo)
                        unicos= self.apagar1s(unicos, self.columnas[y0])
                        self.columnas.pop(y0)
                        break
                    y0=y0+1
        self.renglonesResultado=renglonesResultantes.copy()
        
