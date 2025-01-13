import sys
from collections import deque

readline = sys.stdin.readline

m, n = map(int, readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, readline().split())))



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

days = 0

def bfs(queue):
    nq1 = deque()

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[ny][nx] == -1:
                continue

            if graph[ny][nx] == 1:
                continue

            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                nq1.append((ny, nx))

    return nq1

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
            
a = len(q)
nq = deque()
while a:
    if len(q) > len(nq):
        nq = bfs(q)
    else:
        nq = bfs(nq)
    days += 1
    a = len(nq)


tmp = 0
for i in graph:
    if 0 in i:
        tmp = 1
        break

if tmp:
    print(-1)
else:
    print(days-1)
