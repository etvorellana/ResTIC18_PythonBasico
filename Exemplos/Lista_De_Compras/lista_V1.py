

lista = []

while True:
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Listar itens')
    print('4 - Sair')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        item = input('Digite o item: ')
        lista.append(item)
    elif opcao == 2:
        item = input('Digite o item: ')
        lista.remove(item)
    elif opcao == 3:
        for item in lista:
            print(item)
    elif opcao == 4:
        break
    else:
        print('Opção inválida')

print('Fim do programa')
