from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)

distance[x] = 0
q = deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now]+1
            q.append(next_node)

result = []
for i,d in enumerate(distance):
    if d == k:
        result.append(i)

if result:
    for r in result:
        print(r)
else :
    print(-1)


