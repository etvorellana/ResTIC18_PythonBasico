import random

def sorteio(quantidade):
    lista = []
    for i in range(quantidade):
        sort = random.randint(1, quantidade)
        while sort in lista:
            sort = random.randint(1, quantidade)
        lista.append(sort)
    return lista


def main():

    turma = ["Allana dos Santos Campos", "Arthur Gobira Galvão",
             "Brenndol Pinto Magalhães", "Danilo Silveira da Glória",
             "Erika Ravanna dias Oliveira", "Everaldina Guimarães Barbosa", 
             "Gabriel dos Santos Sousa", "Girleide Macario dos Santos",
             "Ian Robert Luz Pinheiro", "João Manoel Almeida Oliveira",
             "Jose Ulian Cardoso Almeida", "Leane Soares Sousa",
             "Luciano Angelo de Souza Bernardes", "Luis Eduardo Barbosa Soares Rocha",
             "Manoel De Jesus Moura Do Patrocinio", "Marcos Vinicius Tavares Gomes",
             "Matheus Costa Beckerath", "Myllena Souza da Silva",
             "Nairan Bento dos Santos", "Paulo Pereira Marques",
             "Rafaela Cristina Ferreira Brito", "Raíssa Simões de Angelo",
             "Renata Amaral Bamberg", "Ricardo dos Santos Silva",
             "Sérgio de Souza Santos", "Tales de Araujo Cruz",
             "Thiago Alves Sena", "Thiago Carneiro Leite",
             "Vinicius Lima  da SIlva", "Vitor Sousa Pereira"]

    quantidade = len(turma)
    lista = sorteio(quantidade)
    print("Começando as entrevistas...")
    print("Primeiro entrevistado: ", end="")
    for sort in lista:
        print("{} - {}".format(sort, turma[sort-1]))
        input("Aperte ENTER para continuar...")
        if sort != lista[-1]:
            print("Proximo entrevistado: ", end="")
        else:
            print("Fim das entrevistas!")
        

if __name__ == "__main__":
    main()

