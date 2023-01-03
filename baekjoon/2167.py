N, M = list(map(int, input().split()))
array = [list(map(int,input().split()))for i in range(N)]

count = int(input())

for i in range(count):
    ran = list(map(int, input().split()))
    sum = 0
    for j in range(ran[0] - 1, ran[2]):
        for k in range(ran[1] - 1, ran[3]):
            sum = sum + array[j][k]
    print(sum)
