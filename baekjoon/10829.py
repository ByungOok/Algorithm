N = int(input())
binary = []
def binary_change(N) :
    change = N % 2
    binary.append(change)
    if(N // 2 != 0) :
        N = N // 2 
        binary_change(N)
    else : return 1 

binary_change(N)
for i in range(-1, -1*len(binary)-1, -1):
    print(binary[i], end="")