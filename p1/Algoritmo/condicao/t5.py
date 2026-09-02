n1 = float(input("Digite a nota 01: "))
n2 = float(input("Digite a nota 02: "))
n3 = float(input("Digite a nota 03: "))

media = (n1+n2+n3)/3

if media < 7:
    final = float(input("Digite sua nota da final: "))
    

    if final < 5:
        print("Você foi Reprovado")

else:
    print("Você foi APROVADO")