valor_da_compra = float(input("Digite o valor da compra: "))

compra_pix = valor_da_compra * 0.95
compra_cartao = valor_da_compra + (valor_da_compra * 0.08)

print("Valor Pix", compra_pix)
print("Valor Cartao", compra_cartao)