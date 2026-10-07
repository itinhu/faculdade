nota = float(input("Digite uma nota"))

valida = True

while valida:
    if nota>=0 or nota<= 10:
        nota = float(input("Digite uma nota: "))
    else:
        print("Nota inválida.")
        valida = False
