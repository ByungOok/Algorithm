allday = [0]*366
sday = [0]*366
tday = [0]*366
ans_1, ans_2, ans_3, and_4 = 0, 0, 0, 0 

n = int(input())
for i in range (0, n) :
    input = map(list.split())
    start = input[1]
    end = input[2]

    if input[0] == 'T' :
        for j in range(start, end):
            tday[j] = tday[j] + 1
    elif input[0] == 'S':
        for j in range(start,end):
            sday[j] = sday[j] + 1

for i in range (0,366):
    allday[i] = sday[i] + tday[i] 


for i in range(0,366):
    if allday[i] != 0 :
        ans_1 = ans_1 + 1
