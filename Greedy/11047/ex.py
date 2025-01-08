n, k = map(int, input().split())

data = []

for _ in range(n):
    tmp = int(input())
    data.append(tmp)

data.sort()
result = 0

while True:
    for i in range(n-1, -1, -1):
        if k // data[i] != 0:
            if k <= 0:
                break
            tmp = k // data[i]
            k -= (tmp) * data[i]
            result += tmp
    if k <= 0:
        break

print(result)
