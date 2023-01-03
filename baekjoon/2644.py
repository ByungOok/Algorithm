import sys
sys.setrecursionlimit(10**6)

N = int(input())
visited = [False] * (N+1)
num = [0]*(N+1)
family = [[] for i in range (N+1)]
a, b = map(int, input().split())
M = int(input())

for i in range(M) :
    p, s = map(int, input().split())
    family[p].append(s)
    family[s].append(p)

count = 0

def DFS(start) :
    visited[start] = True
    for i in family[start] :
        if not visited[i] :
            num[i] = num[start] + 1
            DFS(i)

DFS(a) 

if  num[b] == 0 :
    print(-1)
else :
    print(num[b])


    """
    while(start != find) :
        global count 
        for i in family[start] :
            if find not in family[i] :
                start = i
                DFS(start, find)
                count += 1
            else :
                count += 1
                find = start 
    """
