valor_boleto = float(input("Digite o valor do boleto: "))

valor_final = valor_boleto + 15

multa = valor_boleto * 0.02

valorfinal = valor_final + multa

print("Valor a pagar: ", valorfinal)