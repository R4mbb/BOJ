import sys
sys.setrecursionlimit(10**9)
readline = sys.stdin.readline


def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if graph[x][y] == "1":
        graph[x][y] = "0"

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x+1, y+1)
        dfs(x-1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y-1)
        return True
    return False


w, h = 1, 1

while True:
    w, h = map(int, input().split())
    graph = []

    for i in range(h):
        graph.append(list(map(str, readline().split())))

    tmp = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                tmp += 1

    if w == 0 and h == 0:
        break

    print(tmp)

