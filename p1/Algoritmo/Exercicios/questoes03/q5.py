paisA = float(input("Digite a população:"))
taxaA = float(input("Digite a taxa de crescimento:"))
paisB = float(input("Digite a população:"))
taxaB = float(input("Digite a taxa de crescimento:"))

anos = 0
while True:
    paisA = paisA * ((taxaA/100)+1)
    paisB = paisB * ((taxaB/100)+1)
    anos = anos + 1
    if paisA >= paisB:
        print("País A igualou com País B e levou: ", anos," anos" )
        break
