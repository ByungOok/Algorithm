N, M = map(int, input().split())
card = list(map(int,input().split()))
orgin = 0
for i in range (0, N) : 
    for j in range(i+1, N) :
        if j == i : continue
        for k in range(j+1, N) :
            if (k == j or k == i) : continue
            sum = card[i] + card[j] + card[k]
            if(sum > M) : continue
            if((M-orgin) > (M-sum)) :
                orgin = sum     
print(orgin)