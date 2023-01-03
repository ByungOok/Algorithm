a = int(input())
b = int(input())
c = int(input())
mul = a*b*c

string = str(mul)

count = [0] * 10

for i in range(0, len(string)):
    for j in range(0, 10):
        if(str(j) == string[i]):
            count[j] += 1

for i in range(0,10):
    print(count[i])

