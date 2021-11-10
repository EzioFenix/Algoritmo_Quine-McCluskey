import renglon
class Tablero():

    def __init__(self,miniterminos:list,oldRenglones:list,indiceDontCare:int):
        self.renglonesHoja=[]
        self.renglonesResultado=[]
        self.miniterminos=miniterminos
        self.indiceDontCare=indiceDontCare
        self.indices={}
        self.columnas=[]
        self.obtenerHojas(oldRenglones)
    
    def arrregloBitsToLetras(self,arreglo:list):
        letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        aux=[]
        for  x0 in range(len(arreglo)):
            if arreglo[x0]=='1':
                aux.append(letras[x0])
            elif arreglo[x0]=='0':
                aux.append(letras[x0]+"'")
        return aux.copy()


    def imprimirV2(self):
        with open("output.txt","a") as f:
            f.write('\n Miniterminos Resultado' + "\n")
            aux=[]
            f.write("{}{}{}".format("┌","─"*83,"┐") + "\n")
            texto="|{:<10} \t│ {:<10} \t│ {:<10} \t│ {:<30} \t│".format("generacion",'indice','bits','miniterminos')
            f.write(texto + "\n")
            f.write("{}{}{}".format("├","─"*83,"┤") + "\n")
            for i in self.renglonesResultado:
                aux.append(i.bits)
                f.write(i.toStr() + "\n")
            f.write("{}{}{}".format("└","─"*83,"┘") + "\n")

            aux2=[self.arrregloBitsToLetras(i) for i in aux]
            aux3=[]
            for i in aux2:
                aux3.append("".join(i))
            aux3=" + ".join(aux3)
            f.write('\n\n fsp=')
            f.write(aux3)


    def imprimir(self):
        aux=[]
        print("{}{}{}".format("┌","─"*87,"┐"))
        texto="|{:<10} \t│ {:<10} \t│ {:<10} \t│ {:<30} \t│".format("generacion",'indice','bits','miniterminos')
        print(texto)
        print("{}{}{}".format("├","─"*87,"┤"))
        for i in self.renglonesResultado:
            aux.append(i.bits)
            print(i)
        print("{}{}{}".format("└","─"*87,"┘"))

        aux2=[self.arrregloBitsToLetras(i) for i in aux]
        aux3=[]
        for i in aux2:
            aux3.append("".join(i))
        aux3=" + ".join(aux3)
        print('\n fsp=',aux3)
    
    def minimizar(self):
        self.crearIndice()
        self.build()
        self.llenarTablero()
        self.seleccionarMiniterminosV2()
        # El minitermino tiene que ser mayores a 0
        if -1<self.indiceDontCare: 
            self.eliminarDontCare()


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


    def seleccionarMiniterminosV2(self):
        """Selecciona a los miniterminos que conforman la minimización total
        """
        with open("output.txt",'a') as f:
            renglonesResultantes=[]
            y=len(self.renglonesHoja)
            x=len(self.indices)

            #En el arreglo unicos, donde tenga un 1 es aquel que sólo hay un minitermino que lo contiene
            #suma los 1's por columnas
            unicos=[]
            for x0 in range(x):
                unicos.append(0)
                for y0 in range(y):
                    unicos[x0]=unicos[x0]+self.columnas[y0][x0]
            
            #----------------------------------------------------
            f.write('\nTabla de implicaciones \n')
            
            texto2=""
            for mini in self.miniterminos:
                texto2 +="│{:<3}".format(str(mini))

            texto="│ {:<30}{}│".format("Implicante primo",texto2)

            numEspacios=len(texto)-2
            f.write("{}{}{}".format("┌","─"*numEspacios,"┐") + "\n")
            f.write(texto + "\n")
            f.write("{}{}{}".format("├","─"*numEspacios,"┤") + "\n") 

            for y0 in range(y):
                textoMiniterminos= self.renglonesHoja[y0].miniterminosStr()

                # convetir columnas
                textoColumnas=[str(i) for i in self.columnas[y0]]
                aux=""
                for i in textoColumnas:
                    aux+="│{:<3}".format(i)

                texto="│ {:<30}{}│".format(textoMiniterminos,aux)
                f.write(texto + "\n")
            f.write("{}{}{}".format("└","─"*numEspacios,"┘") + "\n") 
            #----------------------------------------------------

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



    def seleccionarMiniterminos(self):
        """Selecciona a los miniterminos que conforman la minimización total
        """
        renglonesResultantes=[]
        y=len(self.renglonesHoja)
        x=len(self.indices)

        #En el arreglo unicos, donde tenga un 1 es aquel que sólo hay un minitermino que lo contiene
        #suma los 1's por columnas
        unicos=[]
        for x0 in range(x):
            unicos.append(0)
            for y0 in range(y):
                unicos[x0]=unicos[x0]+self.columnas[y0][x0]
        
        #----------------------------------------------------
        print('\nTabla de implicaciones \n')
        
        texto2=""
        for mini in self.miniterminos:
            texto2 +="│{:<3}".format(str(mini))

        texto="│ {:<30}{}│".format("Implicante primo",texto2)

        numEspacios=len(texto)-2
        print("{}{}{}".format("┌","─"*numEspacios,"┐"))
        print(texto)
        print("{}{}{}".format("├","─"*numEspacios,"┤")) 

        for y0 in range(y):
            textoMiniterminos= self.renglonesHoja[y0].miniterminosStr()

            # convetir columnas
            textoColumnas=[str(i) for i in self.columnas[y0]]
            aux=""
            for i in textoColumnas:
                aux+="│{:<3}".format(i)

            texto="│ {:<30}{}│".format(textoMiniterminos,aux)
            print(texto)
        print("{}{}{}".format("└","─"*numEspacios,"┘")) 
        #----------------------------------------------------

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

    def obtenerArregloDontCare(self)->list:
        indice =self.miniterminos.index(self.indiceDontCare)
        return self.miniterminos[indice:].copy()


    def eliminarDontCare(self):
        y0=0
        arregloDontCare=self.obtenerArregloDontCare()
        while y0 <len(self.renglonesResultado):
            numMiniterminosSimpli=len(self.renglonesResultado[y0].miniterminosSimpli)
            contadorDontCare=0
            for minitermino in self.renglonesResultado[y0].miniterminosSimpli:
                if minitermino in arregloDontCare:
                    contadorDontCare+=1
            if numMiniterminosSimpli==contadorDontCare:
                self.renglonesResultado.pop(y0)
            else:
                y0+=1
                

        
