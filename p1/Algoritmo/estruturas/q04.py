#aça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
consoantes = []
vogais = ['a','e','i','o','u']
for i in range(10):
    letra = input('Digite uma letra:')
    if letra in vogais:
        continue
    else:
        consoantes.append(letra)

print(f'Foram lidas {len(consoantes)} consoantes:')
i = 0
for i in range(len(consoantes)):
    print(consoantes[i])