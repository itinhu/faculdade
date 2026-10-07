paisA = 80000
paisB = 200000
anos = 0
while True:
    paisA = paisA * 1.03
    paisB = paisB * 1.015
    anos = anos + 1
    if paisA >= paisB:
        print("País A igualou com País B e levou: ", anos," anos" )
        break
