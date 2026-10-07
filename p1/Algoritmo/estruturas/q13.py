# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
# lista. Após isto, calcule a
# média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
# e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
temperaturas = []
media = 0
for mes in meses:
    temperatura = float(input(f'Digite a temperatura do mês de {mes}:'))
    temperaturas.append(temperatura)

print('exitResultado das temperaturas:')

for i in range(12):
    print(f'{i+1} - {meses[i]}: {temperaturas[i]}°C')
    media = media + temperaturas[i]
print(f'Média de temperatura: {media/12}°C')