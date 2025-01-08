n = int(input())

data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

data1.sort()
data2.sort(reverse=True)

result = 0

for num, i in enumerate(data1):
    result += i * data2[num]

print(result)
