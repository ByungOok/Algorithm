N, M = map(int, input().split())
array = []
numbers = [i for i in range(1, N+1)]
visited =  [False] * (N+1)

def dfs(start) :
    if len(array) == M :
        for i in range(0, len(array)) :
            print(array[i], end = " ")
        print("")
        return
    
    for i in range(start, N+1) :
        if i not in array :
            array.append(i)
            dfs(i+1)
            array.pop()

def DFS(start) : 
    if len(array) == M:
        for i in range(0, len(array)) :
            print(array[i], end = " ")
        print("")
        return
    for i in range(start, N+1) :
        visited[i] = True
        array.append(i) 
        DFS(i+1)
        array.pop()
        visited[i] =False

DFS(1)