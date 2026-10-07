print('----------Sistema do primeiro ano----------')
alunos = []

while True:
    print('\n----------Menu---------')
    print('1 - Cadastrar aluno')
    print('2 - Listar alunos')
    print('3 - Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        nome = input('Digite o nome do aluno: ')
        alunos.append(nome)
        print(f'Aluno {nome} cadastrado com sucesso!')
    elif opcao == '2':
        print(alunos)
    elif opcao == '3':
        print('Saindo do sistema...')
        break
