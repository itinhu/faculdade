repeticoes = int(input("Digite quantos número irá digitar: "))

menor = float(input("Digite um número: "))

for i in range(repeticoes-1):
    num = float(input("Digite um número: "))
    if num < menor:
        menor = num

print(f'O menor número é {menor}')