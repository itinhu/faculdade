#percorrer lista com for
lista_amigos = ['Italo', 'Maria', 'João', 'Carlos']

nome = input('Digite o nome do amigo que deseja buscar: ')

for amigo in lista_amigos:
    if amigo in nome:
        print(f'{nome} encontrado na lista!')
        break
    else:
        print(f'{nome} não encontrado na lista.')
