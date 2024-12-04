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

similarity_score = 0

for i in range(0,len(col1)):
    current_element = col1[i]
    current_element_count = 0
    for j in range(0,len(col2)):
        if current_element == col2[j]:
            current_element_count+= 1
    similarity_score+=current_element * current_element_count

print(similarity_score)
