import sys
from collections import deque 

N, K = map(int, sys.stdin.readline().split())
queue = deque([])
queue_print = []
for i in range (1, N+1) :
    queue.append(i) 

print("<", end ="")

while queue :
    for i in range(0, K - 1) :
        queue.append(queue.popleft())
    print(queue.popleft(), end = "")
    if queue :
        print(", ", end = "")
print(">")