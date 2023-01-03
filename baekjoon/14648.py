n, q = list(map(int,input().split()))
array = list(map(int,input().split())) #수열 입력
for i in range(0, q) :
    query = list(map(int,input().split()))
    if query[0] == 2:
        result_1,result_2 = 0, 0
        for j in range(query[1] - 1, query[2]) :
            result_1 = result_1 + array[j]
        for j in range(query[3] - 1, query[4]) :
            result_2 = result_2 + array[j]
        result = result_1 - result_2

    elif query[0] == 1:
        result = 0
        for j in range(query[1] - 1, query[2]):
            result = result + array[j]
        temp = array[query[1] - 1]
        array[query[1] - 1] = array[query[2] - 1]
        array[query[2] - 1] = temp

    print(result)
