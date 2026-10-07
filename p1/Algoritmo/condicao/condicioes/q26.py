alcool = float(input("Digite o valor do Etanol: "))
gasolina = float(input("Digite o valor da Gasolina"))

razao = alcool / gasolina

if razao < 0.7:
    print("Abasteça com Etanol")
else:
    print("Abasteça com Gasolina")