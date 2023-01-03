import sys 

N = int(sys.stdin.readline())
rope = [] 
for i in range (N) : 
    rope.append(int(sys.stdin.readline()))

rope.sort() 
rope.reverse()

find = [] 
for i in range(0, N) :
    find.append(rope[i]*(i+1))
print(max(find))
