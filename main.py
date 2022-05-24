import json

def CoinChose(den, camb):
    #Create Dynamic Programming
    coin = len(den)
    amount = camb + 2

    CD = [[0 for j in range(amount)] for i in range(coin)]
    sizeCD = len(CD)

    j = 0
    i = 0
    NewCD = CD


    for i in range(sizeCD):
        NewCD[j][0] = den[i]
        j = j + 1


    for i in range(sizeCD):
        for j in range(len(CD[0])):
            if CD[i][0] == j:
                CD[i][j+1] = 1

    #Crea el 1
    for j in range(3, len(CD[0])):
        CD[0][j] = CD[0][j-1] + 1

    #Crea el resto

    combinations = [[0 for j in range(1,amount)] for i in range(coin)]
    monto = camb
    moneda = len(den)

    # Lo chido
    for i in range(len(CD)):
        for j in range(1,len(CD[0])):
            combinations[i][j-1] = CD[i][j]

    for i in range(moneda):
        for j in range(monto):
            if j >= den[i]:
                for k in range(i, moneda):
                    combinations[k][j] = combinations[i][j-den[i]] + 1



    print(CD)
    print(combinations)

#User Input
den = [1,2,5,10,20]
camb = 10

array = CoinChose(den, camb)
print(array)

#JSON Operation
f = open("coin-change.json")

data = json.load(f)

print(data)

f.close()