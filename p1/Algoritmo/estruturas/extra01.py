alunos = [
    ['João', 7.5],
    ['Maria', 9.0],
    ['Pedro', 5.5],
    ['Ana', 8.0],
    ['Lucas', 6.5]
]

#maior nota
maior_nota = alunos[0][1]
nome_maior_nota = alunos[0][0]
for aluno in alunos:
    if aluno[1] > maior_nota:
        maior_nota = aluno[1]
        nome_maior_nota = aluno[0]

#media das notas
soma = 0

for aluno in alunos:
    soma = soma+aluno[1]
media = soma / len(alunos)

#qtde aprovados
apt = 0
for aluno in alunos:
    if aluno[1]>=7:
        apt = apt + 1

#pesquisa por nome
nome = input('Digite o nome do aluno: ')
achou = False
for aluno in alunos:
    if nome in aluno[0]:
        achou = True
        break
if achou:
    print(f'Aluno {aluno[0]} encontrado')
else:
    print(f'Aluno {nome} não encontrado')