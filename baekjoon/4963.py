import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [ 0, 1, 0,-1,  1, -1,-1, 1]

def dfs(x, y) :
    for i in range(0, 8) :
        new_x = x + dx[i]
        new_y = y + dy[i]
        if((new_x >= 0 and new_x < h) and (new_y >= 0 and new_y < w)):
            if(graph[new_x][new_y] == 1) :
                graph[new_x][new_y] = 0
                dfs(new_x, new_y)

while True : 
    w ,h = map(int, input().split())
    if(w == 0 and h == 0) : break
    graph = []
    count = 0

    for i in range(0, h) :
        graph.append(list(map(int, input().split())))

    for i in range(0, h) :
        for j in range(0, w) :
            if graph[i][j] == 1 :
                count += 1 
                graph[i][j] = 0 
                dfs(i, j)
    print(count)
            