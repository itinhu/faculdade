num = 1
while True:
    print(num)
    num+=1
    if num > 20:
        break

num = 1
num_string = ""
while True:
    num_string = num_string + str(num) + " "
    num += 1
    
    if num > 20:
        break
print(num_string)