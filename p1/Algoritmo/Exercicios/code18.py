saque = int(input("Digite o valor do saque: "))

restante = saque

cedulas_de_100 = saque // 100
restante = saque % 100

cedulas_de_50 = restante // 50
restante = restante % 50

cedulas_de_20 = restante // 20
restante = restante % 20

cedulas_de_10 = restante // 10
restante = restante % 10

cedulas_de_5 = restante // 5
restante = restante % 5

cedulas_de_2 = restante // 2
restante = restante % 2

moedas_de_1 = restante // 1

print("="*25)
print("Contagem de notas:")
print("Notas de 100: ", cedulas_de_100)
print("Notas de 50: ", cedulas_de_50)
print("Notas de 20: ", cedulas_de_20)
print("Notas de 10: ", cedulas_de_10)
print("Notas de 5: ", cedulas_de_5)
print("Notas de 2: ", cedulas_de_2)
print("Moedas de 1: ", moedas_de_1)

print("="*25)

print("Quantidade de notas: ", cedulas_de_100 + cedulas_de_50 + cedulas_de_20 + cedulas_de_10 + cedulas_de_5 + cedulas_de_2 + moedas_de_1)