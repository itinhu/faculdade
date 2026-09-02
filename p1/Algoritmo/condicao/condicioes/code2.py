curso = input("fez curso online? ")
psi = input("Passou no psicologico? ")
toxi = input("o exame toxicologico deu bom? ")
pratica = input("passou na pratica? ")

if curso == 'sim' and psi == 'sim' and toxi == 'sim' and pratica == 'sim':
    print("Passou")
else:
    print("não passou")
