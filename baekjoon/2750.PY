import sys

N = int(input())

array = [int(input()) for i in range(N)]

array.sort()

for i in range(0, N):
    print(array[i])

