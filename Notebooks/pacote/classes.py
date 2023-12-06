

from math import atan2, sin, cos

class Ponto:
    ''' A Classe Ponto é utilizada para ilustrar a implementação de
        classes em Python e instanciação das mesmas pela criação de
        objetos derivados desta classe. Ela implementa um modelo de 
        ponto no plano cartesiano. 
    '''
    # incluímos um novo atributo na definição do corpo da classe
    contador = 0 
    
    
    def __init__(self, pCar = None, pPol = None, outroPonto = None):
        ''' 
            Inicialização de um ponto no plano. Utilizamos coordenadas cartesianas
            e coordenadas polares para representar o ponto em relação à origem do
            sistema de coordenadas. As coordenadas do ponto podem ser fornecidas
            como coordenadas cartesianas, polares ou ainda como outro ponto. Caso os
            valores não sejam definidos o ponto sera criado com 
            coordenadas na origem do sistema de coordenadas.
            Cada ponto criado ganha um id único construído com base
            no atributo contador. O atributo também permite contabilizar 
            quantas instâncias da classe já foram criadas. 
            O construtor pode ser chamado de três formas diferentes:
            1. Utilizando uma dupla com as coordenadas x,y do ponto
            em coordenadas cartesianas: 
            p1 = Ponto(pCar = (1.0,2.3)) 
            2. Utilizando uma dupla com as coordenadas rho,theta do ponto
            em coordenadas polares:
            p1 = Ponto(pPol = (1,3.14))
            3. Utilizando outro ponto:
            p2 = Ponto(outroPonto = p1)
            4. Ou ainda sem parâmetros:
        '''
        if pCar: 
            x, y = pCar
            self.__x = x 
            self.__y = y
            self.__rho, self.__theta = Ponto.cart2pol(self.__x, self.__y)
        elif pPol:
            rho, theta = pPol
            self.__rho = rho
            self.__theta = theta
            self.__x, self.__y = Ponto.pol2cart(self.__rho, self.__theta)
        elif outroPonto and type(outroPonto) == 'Ponto':
            self.__x = outroPonto.__x
            self.__y = outroPonto.__y
            self.__rho = outroPonto.__rho
            self.__theta = outroPonto.__theta
        else:
            self.moveXYPara()
        
        # Acessando o atributo da classe
        Ponto.contador += 1       # Podemos referencia assim
        self._id = "Ponto-" + str(self.contador)   # ou assim

    # métodos da classe
    def cart2pol(x, y):
        rho = (x**2 + y**2)**0.5
        theta = atan2(y, x)
        return rho, theta
    
    def pol2cart(rho, theta):
        x = rho * cos(theta)
        y = rho * sin(theta)
        return x, y
    
    def clonarPonto(self):
        return Ponto((self.__x, self.__y))
        #return Ponto(pCar = (self.__x, self.__y))
        #return Ponto(pPol = (self.__rho, self.__theta))
        #return Ponto(None, (self.__rho, self.__theta))
        #return Ponto(outroPonto = self)
        #return Ponto(None, None, self)

    def moveXYPara(self, x = 0, y = 0):
        ''' Move o ponto para as novas coordenadas (x, y) definidas nos 
            parâmetros de entrada. Caso não sejam definidos os valores 
            das novas coordenadas, o ponto sera deslocado para a origem.
        '''
        self.__x = x
        self.__y = y
        self.__rho, self.__theta = Ponto.cart2pol(self.__x, self.__y)
        
    def moveXPara(self, x = 0):
        '''
        
        '''
        self.__x = x
        self.__rho, self.__theta = Ponto.cart2pol(self.__x, self.__y)
        
    def moveYPara(self, y = 0):
        '''
        
        '''
        self.__y = y
        self.__rho, self.__theta = Ponto.cart2pol(self.__x, self.__y)

    def naOrigem(self):
        '''Move o ponto para a origem do sistema de coordenadas cartesianas.'''
        self.moveXYPara()       
    
    def moveRhoThetaPara(self, rho = 0, theta = 0):
        '''
        
        '''
        self.__rho = rho
        self.__theta = theta
        self.__x, self.__y = Ponto.pol2cart(self.__rho, self.__theta)

    def moveRhoPara(self, rho = 0):
        '''
        
        '''
        self.__rho = rho
        self.__x, self.__y = Ponto.pol2cart(self.__rho, self.__theta)

    def moveThetaPara(self, theta = 0):
        '''
        
        '''
        self.__theta = theta
        self.__x, self.__y = Ponto.pol2cart(self.__rho, self.__theta)
        
    def distânciaAté(self, outroPonto):
        ' Calcula a distância deste ponto até um outro ponto'
        dist = ( (self.__x - outroPonto.__x)**2 + 
                    (self.__y - outroPonto.__y)**2 )**0.5
        return dist