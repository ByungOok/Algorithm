import queue
from re import L
import sys
from collections import deque

str = sys.stdin.readline()
bracket = deque([])
temp = 1 
res = 0 

for i in range(0, len(str)) : #중괄호 일떄 
    if (str[i] == '[' or str[i] == '(') : #여는 것 일때     
        if str[i] == '[' :
            temp *= 3
            bracket.appendleft(str[i]) 
        elif str[i] == '(' :
            temp *= 2
            bracket.appendleft(str[i]) 
    elif (str[i] == ']') : #닫는 것 일때
        if(len(bracket) == 0) : 
            res = 0
            break
        if(bracket.popleft() == '[') : 
            if(str[i-1] == '[') : 
                res += temp 
        else :
            res = 0
            break
        temp = temp // 3

    elif (str[i] == ')') : #소괄호 일때
        if(len(bracket) == 0) : 
            res = 0
            break
        if(bracket.popleft() == '(') :
            if(str[i-1] == '(') : 
                res += temp
        else : 
            res = 0
            break 
        temp = temp // 2

if(len(bracket) == 0) :
    print(res)
else :
    print(0)
