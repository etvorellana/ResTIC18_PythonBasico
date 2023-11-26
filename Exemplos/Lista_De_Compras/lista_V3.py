

def main():

    lista = []
    quant = ['Unidade', 'Kg', 'Litro', 'Pacote', 'Caixa', 'Dúzia', 'Grama', 'Metro', 'Lata', 'Fardo', 'Saco', 'Pote', 'Bandeja'] 

    while True:
        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Listar itens')
        print('4 - Sair')
        opcao = int(input('Digite uma opção: '))
        if opcao == 1:
            item = input('Digite o item: ')
            quantidade = int(input('Digite a quantidade: '))
            while True:
                for i in range(len(quant)):
                    print('{} - {}'.format(i, quant[i]))
                    #print(i, '-', quant[i])
                    #print(f'{i} - {quant[i]}')
                unidade = int(input('Digite a unidade: '))
                if unidade >= len(quant) or unidade < 0:
                    print('Unidade inválida')
                    continue
                break
            lista.append((item, quantidade, quant[unidade]))
        elif opcao == 2:
            item = input('Digite o item: ')
            for listItem in lista:
                if listItem[0] == item:
                    lista.remove(listItem)
                    break
        elif opcao == 3:
            for item in lista:
                print(item)
        elif opcao == 4:
            break
        else:
            print('Opção inválida')

        print('Fim do programa')

# main()

if __name__ == '__main__':
    main()