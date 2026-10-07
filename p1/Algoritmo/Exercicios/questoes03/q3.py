while True:
    nome = input("Digite seu nome:")
    if len(nome)<3:
        print("Nome pequeno demais, digite novamente")
    else:
        break

while True:
    idade = input("Digite sua Idade: ")
    if idade >= 0 and idade <= 150:
        break
    else:
        print("Digite a idade novamente")

while True:
    salario = float(input("Digite seu salário: "))
    if salario < 0:
        print("Digite novamente.")
    else:
        break

while True:
    sexo = input("Digite o seu sexo, f ou m")
    if sexo == "f" or sexo == "m":
        break
    else:
        print("Digite novamente")

while True:
    estado = input("Digite seu estado civil: ")
    if estado == "s" or estado == "c" or estado == "v" or estado == "d":
        break
    else:
        print("Digite novamente.")

print("Nome:", nome, "Idade: ", idade, "Salário: ", salario, "Sexo: ", sexo, "Estado Civil: ", estado)
