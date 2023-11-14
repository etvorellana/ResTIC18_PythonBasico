

lista = []

while True:
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Listar itens')
    print('4 - Sair')
    opcao = int(input('Digite uma opção: '))
    match opcao:
        case 1:
            item = input('Digite o item: ')
            lista.append(item)
        case 2:
            item = input('Digite o item: ')
            lista.remove(item)
        case 3:
            for item in lista:
                print(item)
        case 4:
            break
        case _:
            print('Opção inválida')

print('Fim do programa')