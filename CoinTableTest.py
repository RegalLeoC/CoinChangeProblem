camb = 14
den = [1,2,5,10,20]

table = [[0 for i in range(camb+1)] for j in range(len(den))]

for i in range(1,camb + 1):
    ones = 1 + table[0][i-1]
    table[0][i] = ones

for i in range(1,len(den)):
    add = 1
    for j in range(camb+1):
        if j < den[i]:
            table[i][j] = table[i-1][j]
        elif j == den[i]:
            table[i][j] = 1
        elif j > den[i]:
            table[i][j] = (table[i][j - (j-add)]) + 1
            add = add + 1


print(table)