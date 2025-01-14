from collections import deque
import sys
readline = sys.stdin.readline

n, m = map(int, readline().split())

graph = []
for _ in range(n):
    tmp = []
    for i in readline().rstrip():
        for j in i:
            tmp.append(int(j))
    graph.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))

    return graph[n-1][m-1]

print(bfs(0, 0))
