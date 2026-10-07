qtd_morango = float(input("Digite a quantidade de morangos (em Kg): "))
qtd_maca = float(input("Digite a quantidade de maçãs (em Kg): "))

if qtd_morango <= 5:
    preco_morango = qtd_morango * 2.50
else:
    preco_morango = qtd_morango * 2.20

if qtd_maca <= 5:
    preco_maca = qtd_maca * 1.80
else:
    preco_maca = qtd_maca * 1.50

total_kg = qtd_morango + qtd_maca
valor_total = preco_morango + preco_maca

if total_kg > 8 or valor_total > 25.00:
    valor_total = valor_total * 0.90

print("Valor a ser pago pelo cliente: R$",valor_total)