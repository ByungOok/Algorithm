from collections import deque

N, M, V  = map(int,input().split())

graph = [[] for i in range(0, N+1)]
vst_DFS = [False] * (N+1)
vst_BFS = [False] * (N+1)

for i in range(0, M) :
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def DFS(start) :
    vst_DFS[start] = True
    print(start, end = " ")
    graph[start].sort()
    for i in graph[start] :
        if vst_DFS[i] != True :
            DFS(i)


def BFS(start) :
    vst_BFS[start] = True   
    q = deque([start])
    while q :
        start = q.popleft()
        print(start, end = " ")    
        for i in graph[start] :
            if vst_BFS[i] != True : 
                q.append(i)
                vst_BFS[i] = True 

DFS(V)
print("")
BFS(V)
