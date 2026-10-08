atletas = []

while True:
    nome = input('Digite o nome')
    if nome == '':
        break
    saltos = list()
    for i in range(5):
        salto = float(input('Digite o salto: '))
        saltos.append(salto)
    atletas.append([nome, saltos])
    
print(atletas)

