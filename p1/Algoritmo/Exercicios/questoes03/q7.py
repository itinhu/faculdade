# num = float(input("Digite um número: "))
# maior = num

# for i in range(4):
#     num = float(input("Digite um número: "))
#     if num > maior:
#         maior = num
# print("O maior número é: ", maior)

num = float(input("Digite um número: "))
maior = num
i = 0
while i < 4:
    num = float(input("Digite um número: "))
    i+=1
    if num > maior:
        maior = num

print("O maio número é : ", maior)