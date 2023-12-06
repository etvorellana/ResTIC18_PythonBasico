from pacote import Ponto
#from pacote.classes import Ponto

def ordenaPontos(pontos):
    """Ordena uma lista de pontos em ordem crescente da distância 
    ao centro do sistema de coordenadas.

    Args:
        pontos (list): Lista de pontos

    Returns:
        list: Lista de pontos ordenada
    """
    return sorted(pontos, key=lambda p: p.distânciaAté(Ponto()))