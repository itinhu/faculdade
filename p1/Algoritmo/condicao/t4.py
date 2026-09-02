nota = float(input("Digite a sua nota"))

if nota > 9:
    nota = nota * 1.1
    if nota > 10:
        nota = 10

print("Sua nota final é: ", nota)