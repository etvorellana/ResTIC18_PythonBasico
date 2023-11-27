import objetosGeometricos as og

def main():
    # Vamos criar uns pontos
    '''
       (0,1)       (1,1)
        B|---------C
         |         |
         |         |
         |         |
        A|---------D 
       (0,0)      (1,0)
    ''' 
    pA = og.Ponto((0,0)) 
    pB = og.Ponto((0,1))
    pC = og.Ponto((1,1))
    pD = og.Ponto((1,0))

    # Podemos criar o triangulo ABC como 
    tABC = og.Triangulo((0,0), (0,1), (1,1))
    # mas também podemos criar o triangulo ADC como
    tADC = og.Triangulo(pA, pC, pD)
    # Os dois devem ter o mesmo perimetro
    print("Perimetro ABC = {}".format(tABC.calculaPerimetro()))
    print("Perimetro ADC = {}".format(tADC.calculaPerimetro())) 
    # Agora podemos definir o poligono 
    pABCD = og.Poligono(pA, pB, pC, pD)
    # O perimetro do poligono deve ser 4
    print("Perimetro pABCD = {}".format(pABCD.calculaPerimetro()))


if __name__ == "__main__":
    main()