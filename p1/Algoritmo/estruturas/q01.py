numeros = []

for i in range(5):
    num = int(input(f'Digite o {i+1}° número: '))
    numeros.append(num)

for n in range(len(numeros)):
    print(numeros[n])