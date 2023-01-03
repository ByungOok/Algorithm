import sys

N = int(input())

array = [int(input()) for i in range(N)]

array.sort()
array.reverse()

for i in range(0, N):
    print(array[i])

