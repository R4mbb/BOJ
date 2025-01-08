data = input().split('-')

for num, i in enumerate(data):
    tmp = []
    result2 = 0
    
    if '+' in i:
        tmp = i.split('+')
        for j in tmp:
            result2 += int(j)
        data[num] = str(result2)

for num, i in enumerate(data):
    if num == 0:
        result1 = int(i)
    else:
        result1 -= int(i)

print(result1)
