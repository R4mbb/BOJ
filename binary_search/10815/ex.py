import sys
input = sys.stdin.readline

n = int(input().rstrip())
data1 = list(map(int, input().split()))

m = int(input().rstrip())
data2 = list(map(int, input().split()))


result = [0 for _ in range(m)]

for i in data1:
    if i in data2:
        tmp = data2.index(i)
        result[tmp] = 1

print(*result)
