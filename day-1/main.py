col1,col2 = [],[]

with open("input.txt", "r") as input:
    data = input.read().split()
    for i in range(0,len(data)):
        if i%2==0:
            col2.append(int(data[i]))
        else:
            col1.append(int(data[i]))

col1 = sorted(col1)
col2 = sorted(col2)

sum = 0
for i in range(0,len(col1)):
    pair_diff = abs(col1[i] - col2[i])
    sum+=pair_diff

print(sum)
