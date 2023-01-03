N = int(input())
point = []
for i in range(0, N) :
    point.append(list(map(int,input().split())))

point.sort()

for i in range(0, N):
    print("%d %d" %(point[i][0] ,point[i][1]))
