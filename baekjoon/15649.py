N, M = map(int, input().split())
array = []

def New_DFS() :
    if len(array) == M :
        for i in range(0, len(array)) :
            print(array[i], end = " ")
        print("")
        return 
    for i in range(1, N + 1) :
        #f i not in array :
        array.append(i)
        New_DFS()
        array.pop()

New_DFS()