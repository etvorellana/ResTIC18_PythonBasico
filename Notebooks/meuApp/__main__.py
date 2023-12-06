from . interface import *
from . recursos import cart2pol, pol2cart
def main():
    op = menu()
    while op != 3:
        if op == 1:
            x, y = entradaCartesiana()
            rho, theta = cart2pol(x, y)
            saídaPolar(rho, theta)
        elif op == 2:
            rho, theta = entradaPolar()
            x, y = pol2cart(rho, theta)
            saídaCartesiana(x, y)
        else:
            print('Opção inválida!')
        op = menu()


if __name__ == '__main__':
    main()

