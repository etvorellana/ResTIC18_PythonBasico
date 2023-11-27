from math import atan2, sin, cos

class Ponto:
    ''' 
        Implementa um modelo de ponto no plano que pode ser 
        representado pelos sistema de cordeadas cartesianas 
        ou polares. 
    '''
    
    def __init__(self, pCar = None, pPol = None, outroPonto = None):
        ''' 
            Inicialização de um ponto no plano. Utilizamos o sistema de
            coordenadas cartesianas e coordenadas polares para 
            representar o ponto em relação à origem do sistema de 
            coordenadas. As coordenadas do ponto podem ser fornecidas
            como coordenadas cartesianas, polares ou ainda como outro 
            ponto. 
            Caso os valores não sejam definidos o ponto sera criado com 
            coordenadas na origem do sistema de coordenadas.
            O construtor pode ser chamado de três formas diferentes:
            1. Utilizando uma dupla com as coordenadas x,y do ponto
            em coordenadas cartesianas: 
            p1 = Ponto(pCar = (1.0,2.3)) 
            2. Utilizando uma dupla com as coordenadas rho,theta do 
            ponto em coordenadas polares:
            p1 = Ponto(pPol = (1,3.14))
            3. Utilizando outro ponto:
            p2 = Ponto(outroPonto = p1)
            4. Ou ainda sem parâmetros:
        '''
        # Identificando o modo de inicialização
        if pCar: # equivale a pCar != None
            try:
                x, y = pCar
            except: # se nã0 for uma dupla
                self.moveXYPara() #cria como um ponto na origem
            else:
                self.__x = x 
                self.__y = y
            finally: 
                self.__rho, self.__theta = Ponto.cart2pol(self.__x, self.__y)
        elif pPol:
            try:
                rho, theta = pPol
            except:
                self.moveRhoThetaPara()
            else:
                self.__rho = rho
                self.__theta = theta
            finally:
                self.__x, self.__y = Ponto.pol2cart(self.__rho, self.__theta)
        elif outroPonto and isinstance(outroPonto, Ponto):
            self.__x = outroPonto.__x
            self.__y = outroPonto.__y
            self.__rho = outroPonto.__rho
            self.__theta = outroPonto.__theta
        else:
            self.moveXYPara()
        
    # métodos da classe
    def cart2pol(x, y):
        '''
            Permite converter de coordenadas cartesianas para polares.
        '''
        rho = (x**2 + y**2)**0.5
        theta = atan2(y, x)
        return rho, theta
    
    def pol2cart(rho, theta):
        '''
            Permite converter de coordenadas polares para cartesianas
        '''
        x = rho * cos(theta)
        y = rho * sin(theta)
        return x, y
    
    def clonarPonto(self):
        '''
            Retorna um novo objeto da classe Ponto com as mesmas 
            coordenadas. Ou seja, cria um clone ou copia do objeto
        '''
        # Vaja as implementações possíveis
        return Ponto(pCar = (self.__x, self.__y)) # Chave
        #return Ponto((self.__x, self.__y))         # Posicional
        #return Ponto(pPol = (self.__rho, self.__theta)) 
        #return Ponto(self)  

    def moveXYPara(self, x = 0, y = 0):
        ''' 
            Move o ponto para as novas coordenadas (x, y) definidas nos 
            parâmetros de entrada. Caso não sejam definidos os valores 
            das novas coordenadas, o ponto sera deslocado para a origem.
        '''
        self.__x = x
        self.__y = y
        self.__rho, self.__theta = self.cart2pol(self.__x, self.__y)
        
    def moveXPara(self, x = 0):
        '''
            Move o ponto para a nova coordenada x definida no 
            parâmetro de entrada. Caso não seja definido o valor 
            da nova coordenada, o ponto sera deslocado para a x = 0.
            A coordena y permanece a mesma.
        '''
        self.__x = x
        self.__rho, self.__theta = self.cart2pol(self.__x, self.__y)
        
    def moveYPara(self, y = 0):
        '''
            Move o ponto para a nova coordenada y definida no 
            parâmetro de entrada. Caso não seja definido o valor 
            da nova coordenada, o ponto sera deslocado para a y = 0.
            A coordena x permanece a mesma.
        '''
        self.__y = y
        self.__rho, self.__theta = self.cart2pol(self.__x, self.__y)

    def naOrigem(self):
        '''
            Move o ponto para a origem do sistema de coordenadas 
            cartesianas.
        '''
        self.moveXYPara()       
    
    def moveRhoThetaPara(self, rho = 0, theta = 0):
        '''
            Move o ponto para as novas coordenadas (rho, theta) definidas
            nos parâmetros de entrada. Caso não sejam definidos os 
            valores das novas coordenadas, o ponto sera deslocado para 
            a origem.
        '''
        self.__rho = rho
        self.__theta = theta
        self.__x, self.__y = self.pol2cart(self.__rho, self.__theta)

    def moveRhoPara(self, rho = 0):
        '''
            Move o ponto para a nova coordenada rho definida no 
            parâmetro de entrada. Caso não seja definido o valor 
            da nova coordenada, o ponto sera deslocado para a rho = 0.
            A coordena theta permanece a mesma.
        '''
        self.__rho = rho
        self.__x, self.__y = self.pol2cart(self.__rho, self.__theta)

    def moveThetaPara(self, theta = 0):
        '''
            Move o ponto para a nova coordenada theta definida no 
            parâmetro de entrada. Caso não seja definido o valor 
            da nova coordenada, o ponto sera deslocado para a theta = 0.
            A coordena rho permanece a mesma.
        '''
        self.__theta = theta
        self.__x, self.__y = self.pol2cart(self.__rho, self.__theta)

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def rho(self):
        return self.__rho

    @property
    def theta(self):
        return self.__theta
        
    def distânciaAté(self, outroPonto):
        ''' 
            Calcula a distância deste ponto até um outro ponto
        '''
        dist = ( (self.__x - outroPonto.__x)**2 + 
                    (self.__y - outroPonto.__y)**2 )**0.5
        return dist
    
    def __repr__(self):
        return f'Ponto("pCar = " ({self.__x}, {self.__y}))'
    
    def __str__(self):
        saída = f"Ponto(x = {self.__x}, y = {self.__y}, "
        saída = saída + f"rho = {self.__rho}, theta = self. __theta)"
        return saída
    
    def __eq__(self, outroPonto):
        if isinstance(outroPonto, Ponto):
            return self.__x == outroPonto.__x and \
                    self.__y == outroPonto.__y

class Triangulo:

    def __init__(self, a = (0, 0), b = (1, 1), c = (1, 0) ):
        if isinstance(a, Ponto):
            self.__a = Ponto(outroPonto = a)
        else:
            self.__a = Ponto(a)
        if isinstance(b, Ponto):
            self.__b = Ponto(outroPonto = b)
        else:
            self.__b = Ponto(b)
        if isinstance(c, Ponto):
            self.__c = Ponto(outroPonto = c)
        else:
            self.__c = Ponto(c)

    def calculaPerimetro(self):
        ladoAB = self.__a.distânciaAté(self.__b)
        ladoBC = self.__b.distânciaAté(self.__c)
        ladoCA = self.__c.distânciaAté(self.__a)
        return ladoAB + ladoBC + ladoCA 
    
    def calculaArea(self):
        '''
            Das aulas de Geometria Analítica temos que:
            1- Pois pontos definem a equação de uma reta. Podemos
            então definir a equação da reta que passa pelos vértices
            a e b do triângulo: Rab.
            2- Dado um ponto e a equação de uma reta, podemos 
            determinar a distância de um ponto à reta. Desta forma
            podemos determinar a altura do ladoAB como a distância
            do vértice c à reta Rab. 
            3- Podemos agora calcular a área do triângulo utilizando
            como base o ladoAB e a altura do mesmo.
            Pesquise e Implemente 
        '''
        pass

    def __str__():
        pass

    def __repr__(self):
        pass

    def __eq__(triangulo):
        pass


class Poligono:

    def __init__(self, *listaCoordenadas):
        self.__vertices = []
        for vertice in listaCoordenadas:
            if isinstance(vertice, Ponto):
                self.__vertices.append(Ponto(outroPonto=vertice))
            else:
                self.__vertices.append(Ponto(vertice))
    
    def calculaPerimetro(self):
        per = 0
        verA = self.__vertices[0]
        for verB in self.__vertices[::-1]:
            per += verB.distânciaAté(verA)
            verA = verB
        return per



