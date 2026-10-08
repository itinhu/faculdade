num = []

for i in range(14,56):
    num.append(i)

for i in range(len(num)):
    if num[i] != 25:
        num[i] = 'a'

print(num)