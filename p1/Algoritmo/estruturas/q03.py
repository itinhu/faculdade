#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
media = 0

for i in range(4):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(nota)

for n in range(4):
    print(f'{n}ª nota: ', notas[n])
    media = media + notas[n]

print(f'Média final é :{media/4}')