N = int(input())
P = list(map(int,input().split()))
P.sort()
H = [0] * N 
sum = 0 
hap = 0
for i in range(0, N) :
    sum = sum + P[i] 
    H[i] = sum 
    hap = hap + H[i]
print(hap)