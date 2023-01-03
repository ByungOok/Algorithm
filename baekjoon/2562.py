arr = list(range(1,31))

for i in range(0, 28):
    x = arr.index(int(input()))
    arr.pop(x)

arr.sort()
print(arr[0])
print(arr[1])
