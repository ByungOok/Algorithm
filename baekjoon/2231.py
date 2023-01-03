N = int(input())
answer = 0
for i in range(1,1000000) :
    i_str = str(i)
    strsum = 0
    for j in range(0, len(i_str)) :
        strsum = strsum + int(i_str[j])
    
    if(N == i + strsum) :
        answer = i
        break

print(answer)