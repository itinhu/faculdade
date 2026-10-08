so = ['xp','7','vista','8','10','11']
campo = input('qual SO deseja mudar?')
ind = -1
for i in range(len(so)):
    if so[i] == campo:
        ind = i

if ind == -1:
    print('O SO digitado não está presente na lista')
else:
    novo = input('digite o SO que vai substituir: ')
    so[ind] = novo
    print(so)

