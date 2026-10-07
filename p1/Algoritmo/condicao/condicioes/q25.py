telefonou = input("Telefonou pra a vítima? ")
local = input("Esteve no local? ")
mora_perto = input("Mora perto? ")
devia = input("Devia pra vítima? ")
trabalhou = input("Já trabalhou com a vítima? ")

soma = 0

if telefonou == "sim":
    soma = soma +1
if local == "sim":
    soma = soma +1
if mora_perto == "sim":
    soma = soma +1
if devia == "sim":
    soma = soma +1
if trabalhou == "sim":
    soma = soma +1

if soma == 2:
    print("Suspeito")
if soma == 3 or soma == 4:
    print("Cúmplice")
if soma == 5:
    print("Assassino")
if soma < 2:
    print("Inocente")