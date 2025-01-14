import sys
from collections import deque
readline = sys.stdin.readline

n = int(readline().rstrip())
count = int(readline().rstrip())

graph = deque()
for _ in range(count):
    a, b = map(int, readline().split())
    graph.append([a, b])

visited = []
graph = deque(sorted(graph))
print(graph)
result = 0

def bfs(graph, visited):
    global result

    while graph:
        v1, v2 = graph.popleft()

        print(graph)
        print(f"v1 : {v1}, v2 : {v2}")
        print(visited)
        print()

        if v1 in visited or v2 in visited:
            visited.append(v1)
            visited.append(v2)
            result += 1
            print(f"result : {result}")

v1, v2 = graph.popleft()
visited.append(v1)
visited.append(v2)

bfs(graph, visited)
print(result)
