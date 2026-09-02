salario = float(input("Digite o salario: "))

if salario <= 280 :
    aum = 0.2
if salario > 280 and salario <= 700:
    aum = 0.1
if salario >700 and salario <=1500:
    aum = 0.1
if salario > 1500:
    aum = 0.05

valor_aum = salario * aum

final = salario + valor_aum

print("Salario antes", salario)
print("Total percentual do aumento", aum * 100)
print("Aumento", valor_aum)
print("Final", final)