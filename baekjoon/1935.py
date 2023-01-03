N = int(input())
str = input()
str_list = list(str)
alphabet = []
oper = []
var = [] 

for i in range(N) :
    alphabet.append(int(input()))
    
count = 0

for i in range(0, len(str_list)) :
    if str_list[i] == "*" :
        var[-2] = var[-2] * var[-1] 
        var.pop()
    elif str_list[i] == "/" :
        var[-2] = var[-2] / var[-1]
        var.pop()
    elif str_list[i] == "+" :
        var[-2] = var[-2] + var[-1]
        var.pop()
    elif str_list[i] == "-" :
        var[-2] = var[-2] - var[-1]
        var.pop()
    else : 
        var.append(alphabet[ord(str_list[i]) - 65])

print("{:.2f}".format(var[0]))