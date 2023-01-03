import sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for j in range(N+1)]
parent = [0 for i in range(N+1)]

for i in range(N - 1) :
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, parent) :
    for i in graph[start] :
        if parent[i] == 0 :
            parent[i] = start
            dfs(i, parent)

dfs(1, parent)

for i in range(2, N+1):
    print(parent[i])
