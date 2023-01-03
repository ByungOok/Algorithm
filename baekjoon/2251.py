from collections import deque 

A, B, C = map(int,input().split())
max = max(A,B,C)
C_water = [] 
visit = [[False]*(max+1) for i in range(max+1)]

def pour(x, y) :
    if not visit[x][y] :
        visit[x][y] = True 
        q.append((x,y))

def BFS() :
    while q : 
        a, b = q.popleft() 
        c = C - a - b

        if a == 0 :
            C_water.append(c)

        water = min(a, B-b)
        pour(a - water, b + water)

        water = min(a, C-c)
        pour(a - water, b)

        water = min(b, A-a)
        pour(a + water, b - water)

        water = min(b, C-c)
        pour(a, b - water)

        water = min(c, B-b)
        pour(a, b + water)

        water = min(c, A-a)
        pour(a + water, b)

q = deque()
q.append((0,0))
BFS()
result = list(set(C_water))
result.sort()
for i in range(len(result)) :
    print(result[i], end = " ")