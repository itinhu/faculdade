#faça um programa que leia a idade de uma pessoa
#idade entre 18 a 34

idade = int(input("Digite sua idade: "))

if idade < 18 or idade > 34:
    print("Vc está fora")
else:
    print("Vc está dentro")