omok = [list(map(int, input().split())) for i in range(19)]
win = 0 
for i in range(0, 15) :
    for j in range(0, 15) :
        if(omok[i][j] == omok[i][j+1] == omok[i][j+2] == omok[i][j+3] == omok[i][j+4] == 1):
            if((j > 0 and omok[i][j-1] == omok[i][j]) or (j < 14 and omok[i][j+5] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 1
            break

        elif(omok[i][j] == omok[i+1][j] == omok[i+2][j] == omok[i+3][j] == omok[i+4][j] == 1) :
            if((i > 0 and omok[i-1][j] == omok[i][j]) or (i < 14 and omok[i+5][j] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 1
            break

        elif(omok[i][j] == omok[i+1][j+1] == omok[i+2][j+2] == omok[i+3][j+3] == omok[i+4][j+4] == 1) :
            if(((i > 0  and j > 0) and omok[i-1][j-1] == omok[i][j]) or ((i < 14 and j < 14)and omok[i+5][j+5] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 1
            break

        elif(omok[i][j] == omok[i][j+1] == omok[i][j+2] == omok[i][j+3] == omok[i][j+4] == 2):
            if((j > 0 and omok[i][j-1] == omok[i][j]) or (j < 14 and omok[i][j+5] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 2
            break

        elif(omok[i][j] == omok[i+1][j] == omok[i+2][j] == omok[i+3][j] == omok[i+4][j] == 2) :
            if((i > 0 and omok[i-1][j] == omok[i][j]) or (i < 14 and omok[i+5][j] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 2
            break

        elif(omok[i][j] == omok[i+1][j+1] == omok[i+2][j+2] == omok[i+3][j+3] == omok[i+4][j+4] == 2) :
            if(((i > 0  and j > 0) and omok[i-1][j-1] == omok[i][j]) or ((i < 14 and j < 14) and omok[i+5][j+5] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 2
            break

for i in range(0, 15) :
    for j in range(4, 19) :
        if (omok[i][j] == omok[i+1][j-1] == omok[i+2][j-2] == omok[i+3][j-3] == omok[i+4][j-4] == 1) :
            if(((i > 0 and j < 18) and (omok[i-1][j+1] == omok[i][j])) or ((i < 15 and j > 4) and (omok[i+5][j-5] == omok[i][j]))) : continue
            print(omok[i][j])
            print("%d %d" %(i+5, j-3))
            win = 1
            break
        if (omok[i][j] == omok[i+1][j-1] == omok[i+2][j-2] == omok[i+3][j-3] == omok[i+4][j-4] == 2) :
            if(((i > 0 and j < 18) and (omok[i-1][j+1] == omok[i][j])) or ((i < 15 and j > 4) and (omok[i+5][j-5] == omok[i][j]))) : continue
            print(omok[i][j])
            print("%d %d" %(i+5, j-3))
            win = 2
            break

for i in range(15, 19) :
    for j in range(0, 15) :
        if(omok[i][j] == omok[i][j+1] == omok[i][j+2] == omok[i][j+3] == omok[i][j+4] == 1):
            if((j > 0 and omok[i][j-1] == omok[i][j]) or (j < 14 and omok[i][j+5] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 1
            break
        elif(omok[i][j] == omok[i][j+1] == omok[i][j+2] == omok[i][j+3] == omok[i][j+4] == 2):
            if((j > 0 and omok[i][j-1] == omok[i][j]) or (j < 14 and omok[i][j+5] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 2
            break

for i in range(0, 15) :
    for j in range(15, 19) : 
        if(omok[i][j] == omok[i+1][j] == omok[i+2][j] == omok[i+3][j] == omok[i+4][j] == 1) :
            if((i > 0 and omok[i-1][j] == omok[i][j]) or (i < 14 and omok[i+5][j] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 1
            break
        elif(omok[i][j] == omok[i+1][j] == omok[i+2][j] == omok[i+3][j] == omok[i+4][j] == 2) :
            if((i > 0 and omok[i-1][j] == omok[i][j]) or (i < 14 and omok[i+5][j] == omok[i][j])) : continue 
            print(omok[i][j])
            print("%d %d" %(i+1, j+1))
            win = 2
            break

if win == 0 :
    print(win)  