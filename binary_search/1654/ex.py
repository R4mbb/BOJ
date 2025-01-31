import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    tmp = input().rstrip()
    data.append(int(tmp))

start = 0
end = max(data)

result = 0
count = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2

    for i in data:
        if i > mid:
            total += i - mid
            count += 1

    if count == m:
        break

    if total < m:
        end = mid - 1
    else:
        result += 1
        start = mid + 1

print(count, result)
