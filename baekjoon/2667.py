import sys
from collections import deque

N = int(input())
house = [list(map(int, input().strip())) for _ in range(N)]
visit = [[False]*N for i in range(N)]
house_count = []

def BFS(y, x) :
    point = (y, x)
    visit[y][x] = True 
    q = deque([point])
    count = 1
    while q :
        curr = q.popleft()
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)] : 
            next = (curr[0] +dy, curr[1] + dx)
            if (0 <= next[0] < N and 0 <= next[1] < N) and house[next[0]][next[1]] == 1 and visit[next[0]][next[1]] != True :
                q.append((next))
                visit[next[0]][next[1]] = True
                count += 1
    house_count.append(count)

for i in range(N) :
    for j in range(N) :
        if house[j][i] == 1 and visit[j][i] != True:
            BFS(j, i)

house_count.sort()
print(len(house_count))
for i in range(len(house_count)) :
    print(house_count[i])