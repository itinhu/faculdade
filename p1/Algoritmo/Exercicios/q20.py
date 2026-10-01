contador = 1
impar = 0
par = 0
while contador <= 10:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    contador += 1

print("Quantidade de números pares: ", par)
print("Quantidade de números ímpares: ", impar)