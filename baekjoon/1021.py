from collections import deque 

N, M = map(int, input().split())
numlist = deque([])
for i in range(1, N + 1) :
    numlist.append(i) 

findlist = list(map(int, input().split()))

count = 0 

for i in range(0, M) : 
    find = findlist[i] 
    f_index = numlist.index(find) 
    while numlist[0] != find :
        if(f_index < len(numlist)/2) : 
            numlist.append(numlist.popleft())
            count += 1
        else : 
            numlist.appendleft(numlist.pop())
            count += 1
    numlist.popleft()
print(count)