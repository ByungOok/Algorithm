import sys

arr = [int(input()) for i in range(0,9)]

sum_list = sum(arr)
gap = sum_list - 100

for i in range(0,9):
    for j in range(0,9):
        if(arr[i] + arr[j] == gap and i != j):
            a = arr[i]
            b = arr[j]

arr.remove(a)
arr.remove(b)

for i in range(0, len(arr)):
    print(arr[i])
    i += 1




