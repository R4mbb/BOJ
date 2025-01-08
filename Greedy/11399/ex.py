n = int(input())
data = list(map(int, input().split()))

result1 = 0
result2 = 0
data.sort()
for i in range(n):
    result1 += data[i]
    result2 += result1

print(result2)

