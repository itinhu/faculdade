num  = int(input("Digite um número: "))
resposta = input("Esse número é par? ")

if num % 2 == 0 and resposta == "sim":
    print('Este número é par. E vc acetou')
if num % 2 == 1 and resposta == "sim":
    print('Este número é impar. E vc errou')
if num % 2 == 0 and resposta == "nao":
    print('Este número é par. E vc errou')
if num % 2 == 1 and resposta == "nao":
    print('Este número é impar. E vc acertou')