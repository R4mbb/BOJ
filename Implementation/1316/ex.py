n = int(input())
data = []

for _ in range(n):
    data.append(input())

result = 0

for i in data:
    legacy = ""

    for num, j in enumerate(i):
        legacy += j

        if num+1 >= len(i):
            break

        if i[num+1] == j:
            continue
        elif legacy[-1:] in i[num+1:]:
            result += 1
            break

print(n-result)



        

