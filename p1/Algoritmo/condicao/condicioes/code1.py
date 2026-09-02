altura = float(input("Digite sua altura: "))
peso = float(input("qual o peso? "))
idade = int(input("Digite sua idade: "))
quer = input("Quer dançar? ")

if altura > 1.60 and peso > 40 and idade >= 18 and quer == 'sim':
    print("Bora simbora")
else:
    print("Vou ali...")