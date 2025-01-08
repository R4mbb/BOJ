import time
n = int(input())
data = list(map(int, input().split())) + [0, 0]

result = 0

a = time.time()
for i in range(n):
    if data[i+1] > data[i+2]:
        tmp = min(data[i], data[i+1]-data[i+2])
        data[i] -= tmp
        data[i+1] -= tmp
        result += tmp*5

        tmp = min(data[i], data[i+1], data[i+2])
        data[i] -= tmp
        data[i+1] -= tmp
        data[i+2] -= tmp
        result += tmp*7
    else:
        tmp = min(data[i], data[i+1], data[i+2])
        data[i] -= tmp
        data[i+1] -= tmp
        data[i+2] -= tmp
        result += tmp*7

        tmp = min(data[i], data[i+1])
        data[i] -= tmp
        data[i+1] -= tmp
        result += tmp*5
    
    result += data[i]*3
    data[i] = 0

print(result)

a = time.time() - a
print(a)
