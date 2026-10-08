op = -1
bandas = []
while op != 0:
    print('\n-----FESTIVAL-----')
    print('1-cadastrar banda')
    print('2-remover banda')
    print('3 listar bandas')
    op = int(input('Digite a opção desejada'))

    if op == 1:
        banda = input('Digite o nome da banda: ')
        bandas.append(banda)
    elif op == 2:
        banda = input('Digite o nome da banda que quer remover')
        for i in range(len(bandas)):
            if bandas[i] == banda:
                bandas.pop(i)
                break
            print('banda não encontrada')
    elif op == 3:
        for banda in bandas:
            print(banda)
    else:
        break
