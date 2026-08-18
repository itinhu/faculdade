#construa um algoritmo em python que leia a idade do usuário e o salario dele. o programa deve dobrar o salario do usuário e somar com o triplo da idade, exiba o salário final
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))

salario = salario * 2
idade = idade * 3

salario_final = salario + idade
print("O seu salário final é R$", salario_final)