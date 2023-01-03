N = int(input())
arr = list(map(int, input().split()))

max_arr = max(arr)
sum = 0

for i in range(0, len(arr)):
    arr[i] = arr[i] / max_arr * 100
    sum = sum + arr[i]

avg = sum / N
print(avg)
