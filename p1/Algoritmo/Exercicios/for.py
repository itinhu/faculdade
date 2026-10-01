#construa um programa 150 pessoas e verifique se o 
marias = 0
for i in range(5):
    nome = input("Digite o nome: ")
    if nome == 'maria':
        marias+=1
    if nome == 'fim':
        break

print(f'A quantidade de Marias é {marias}')
