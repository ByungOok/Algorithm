N = int(input())

matrix = []

for i in range(N):    
	matrix.append(list(map(int, input().split())))

m_count = 0
z_count = 0 
p_count = 0

def paper_check(n, x, y) :
    global m_count
    global z_count
    global p_count
    temp = matrix[x][y]
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if(matrix[i][j] != temp) :
                for a in range(0, 3) :
                    for b in range(0, 3) : 
                        paper_check(n // 3, x + n // 3 * a, y + n // 3 * b)
                return
    if temp == -1 :
        m_count += 1
    elif temp == 0 :
        z_count += 1
    elif temp == 1 :
        p_count += 1
    
paper_check(N, 0, 0)

print(m_count)
print(z_count)
print(p_count)
