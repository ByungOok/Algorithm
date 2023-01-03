S = input() 

def Pelidrop(A) : 
    if(A[::] == A[::-1]) :  
        result = len(A)
        return result

    for i in range (0,len(A)-1):
        if(A[i::] == A[:i-1:-1]):
            Check = i
            result = len(A) + Check
            return result

    for i in range (1,len(A)):
        New_A = A[::] + A[-2:-2-i:-1]
        if(New_A[::] == New_A[::-1]) : 
            result = len(S) + i
            return result

result = Pelidrop(S)
print(result)