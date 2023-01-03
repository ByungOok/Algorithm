N, K = map(int, input().split())
list = []
coin = 0 

for i in range(0, N):
    list.append(int(input()))

for i in range(N-1, -1, -1):
    if(K // list[i] > 0):
        check = i
        break 

for i in range(check, -1, -1):
    this_coin = K // list[i]
    K = K - this_coin * list[i]
    coin = coin + this_coin
    if(K == 0) : break

print(coin)