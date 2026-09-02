nome1 = input("Digite o nome da pessoa 01: ")
altura1 = float(input("Digite a altura da pessoa 01: "))

nome2 = input("Digite o nome da pessoa 02: ")
altura2 = float(input("Digite a altura da pessoa 02: "))

if altura1>altura2:
    print(nome1 + " é maior que " + nome2)
else:
    print(nome2 + " é menor ou igual a "+ nome1)