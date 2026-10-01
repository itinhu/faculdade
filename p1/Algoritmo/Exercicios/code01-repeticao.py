qtde = 0
nome = ''
while True:
    nome = input('Digite o nome: ')
    if nome == 'rafael':
        continue
    if nome == 'fim':
        break
    qtde = qtde + 1

print('a quantidade foi ',qtde)