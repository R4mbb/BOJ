import sys
from collections import deque

readline = sys.stdin.readline

m, n, k = map(int, readline().split())
data = []

for i in range(k):
    data.append(list(map(int, readline().split())))

graph = [[0] * n for _ in range(m)]

for i in data:
    x1, y1 = i[0], m-i[1]
    x2, y2 = i[2], m-i[3]

    if x1 > x2:
        x2 = i[0]
        x1 = i[2]
    if y1 > y2:
        y2 = m-i[1]
        y1 = m-i[3]

    for j in range(x1, x2):
        for o in range(y1, y2):
            graph[o][j] = -1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
count = 0

def bfs(x, y):
    qeueu = deque()
    qeueu.append((y, x))
    result.append(1)
    global count

    while qeueu:
        y, x = qeueu.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[ny][nx] != 0:
                continue
            
            graph[ny][nx] = 1

            result[count] += 1
            qeueu.append((ny, nx))
            continue
    count += 1



for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] += 1
            bfs(j, i)
 
result.sort()
print(len(result))
print(*result)
