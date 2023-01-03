N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

now_oil = price[0]
sum_price = 0

for i in range(0, N-1) : 
    if (price[i] < now_oil) : 
        now_oil = price[i] 
    sum_price = sum_price + now_oil * distance[i]

print(sum_price)