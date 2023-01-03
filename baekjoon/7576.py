from collections import deque 

d = [(0, -1), (0, 1), (1, 0), (-1,0)]

def BFS() :
    while q : 
        curr = q.popleft()
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)] :
            new_y = curr[0] + dy
            new_x = curr[1] + dx 
            if((0 <= new_y < N) and (0 <= new_x < M) and visit[new_y][new_x] == 0 and box[new_y][new_x] == 0) :
                box[new_y][new_x] = 1
                visit[new_y][new_x] = visit[curr[0]][curr[1]] + 1 
                q.append((new_y,new_x))

def result() :
    max = 0
    for j in range(N) :
        for i in range(M) :
            if box[j][i] == 0 :
                print("-1")
                return
            if visit[j][i] > max :
                max = visit[j][i] 
    print(max - 1)
    return 
        
    

M, N = map(int, input().split())
box = [list(map(int,input().split())) for i in range(N)]
visit = [[0]*M for i in range(N)]
count = 0 
q = deque([])

for j in range(N) :
    for i in range(M) :
        if box[j][i] == 1 and visit[j][i] == 0 :
            point = (j,i)
            q.append(point)
            visit[j][i] = 1 

BFS()
result()

