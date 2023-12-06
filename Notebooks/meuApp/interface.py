
def menu():
    print('1 - Cartesianas para Polares')
    print('2 - Polares para Cartesianas')
    print('3 - Sair')
    return int(input('Escolha uma opção: '))

def entradaCartesiana():
    x = float(input('Digite o valor de x: '))
    y = float(input('Digite o valor de y: '))
    return x, y

def entradaPolar():
    rho = float(input('Digite o valor de rho: '))
    theta = float(input('Digite o valor de theta: '))
    return rho, theta

def saídaCartesiana(x, y):
    print('x =', x)
    print('y =', y)

def saídaPolar(rho, theta):
    print('rho =', rho)
    print('theta =', theta)

