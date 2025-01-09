import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())

graph1 = []
graph2 = []
for i in range(n):
    tmp = list(input().rstrip())
    graph1.append(tmp.copy())
    graph2.append(tmp.copy())

rgb1 = ["R", "G", "B"]
result1 = 0
result2 = 0

def dfs1(x, y, color):
    if x < 0 or x >= n or y < 0 or y >= n or graph1[x][y] == "0":
        return False

    if graph1[x][y] == color:
        graph1[x][y] = "0"

        dfs1(x+1, y, color)
        dfs1(x, y+1, color)
        dfs1(x-1, y, color)
        dfs1(x, y-1, color)
        return True
    return False



def dfs2(x, y, color):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if color == "R" or color == "G":
        if graph2[x][y] == "R" or graph2[x][y] == "G":
            graph2[x][y] = "0"

            dfs2(x-1, y, color)
            dfs2(x, y-1, color)
            dfs2(x+1, y, color)
            dfs2(x, y+1, color)
            return True
    elif color == "B":
        if graph2[x][y] == "B":
            graph2[x][y] = "0"

            dfs2(x-1, y, color)
            dfs2(x, y-1, color)
            dfs2(x+1, y, color)
            dfs2(x, y+1, color)
            return True
    return False



for i in range(n):
    for j in range(n):
        for k in rgb1:
            if dfs1(i, j, k) == True:
                result1 += 1

            if dfs2(i, j, k) == True:
                result2 += 1

print(result1, result2)

