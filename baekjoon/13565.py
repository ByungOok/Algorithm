import sys
sys.setrecursionlimit(10**6)

def DFS(y, x) :
    graph[y][x] = 2
    for i in range(4) :
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (0 <= new_x < N) and (0 <= new_y < M) and (graph[new_y][new_x] == 0):
            DFS(new_y, new_x)

M, N = map(int, input().split())
graph = [list(map(int,input())) for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

for i in range(N) :
    if(graph[0][i] == 0) :
        DFS(0, i)

if 2 in graph[M-1] :
    print("YES")
else :
    print("NO")
