import sys

n = int(sys.stdin.readline())
n2 = 0

result = 0

tmp1 = n // 5
tmp2 = n % 5

while True:
    if tmp2 == 0:
        result += tmp1
        print(result)
        break
    elif tmp2%3 == 0:
        result += tmp1 + (tmp2//3)
        print(result)
        break
    tmp1 -= 1
    tmp2 += 5

    if tmp1 < 0:
        print(-1)
        break
