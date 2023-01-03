a = -1 
while (a != 0) :
    a = int(input())
    new_a = str(a)
    pel = True
    for i in range (len(new_a)) :
        if new_a[i] != new_a[-i-1] :
            pel = False
    if a != 0 :
        if pel == True :
            print("yes")
        else :
            print("no")
            