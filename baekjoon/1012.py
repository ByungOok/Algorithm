from collections import deque
import sys

def BFS(y, x, baechu, vst) :
    start = (y,x)
    M, N = len(baechu[0]), len(baechu)
    q = deque([start])
    while q : 
        curr = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)] :
            next = (curr[0] +dy, curr[1] + dx)
            if (0 <= next[0] < N and 0 <= next[1] < M) and baechu[next[0]][next[1]] == 1 and vst[next[0]][next[1]] != True :
                q.append((next))
                vst[next[0]][next[1]] = True

T = int(input())
for i in range(T) :
    M, N, K =  map(int, input().split())
    baechu = [[0]*M for i in range(N)]
    for j in range(K) :
        A, B = map(int, input().split())
        baechu[B][A] = 1 
    vst = [[False]*M for i in range(N)]
    count = 0 
    for y in range (N) :
        for x in range(M) :
            if baechu[y][x] == 1 and vst[y][x] != True:
                vst[y][x] == True 
                BFS(y, x, baechu, vst)
                count += 1 
    print(count)

    