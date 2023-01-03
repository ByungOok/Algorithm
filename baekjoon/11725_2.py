import sys
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for i in range(N+1)]
parent = [0 for _ in range(N+1)]

for i in range (0, N - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 
def DFS(now, parent) :
    for i in graph[now] :
        if parent[i] == 0 :
            parent[i] = now
            DFS(i, parent)

DFS(1, parent)

for i in range(2, N+1) :
    print(parent[i])
