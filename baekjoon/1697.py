from collections import deque
from re import L 
import sys

N, K = map(int, input().split())
count = 0 
max = 10**5
visit = [0] * (max + 1)
# 1칸 앞으로 가거나
# 1칸 뒤로 가거나
# 2배로 가거나 
        
def plus(i) :
    result = i + 1
    return result
def minus(i) :
    result = i - 1
    return result
def mul(i) :
    result = i * 2 
    return result

def BFS(now ,end) :
    q = deque([now])
    q.append(now)
    while q :
        curr = q.popleft()
        if curr == end :
            print(visit[curr])
            break
        for i in (plus(curr), minus(curr), mul(curr)) :
            if 0 <= i and i < max + 1 :
                if visit[i] == 0:
                    q.append(i)
                    visit[i] = visit[curr] + 1 

BFS(N, K)

