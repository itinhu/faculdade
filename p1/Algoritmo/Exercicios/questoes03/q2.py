while True:
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    if nome == senha:
        print("usuário logado.")
        break
    else:
        print("não logado, digite novamente.")