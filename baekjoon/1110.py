N = int(input())

orign = list(str(N))

if(N<10):
    orign.insert(0,0)

change = list()
cycle = 0
temp = orign

while(orign != change):
    sum = int(temp[0]) + int(temp[1])
    sumlist = list(str(sum))
    change = temp[-1] + sumlist[-1] 
    temp = change
    cycle = cycle + 1

print(cycle)




