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

    # for i in range(sizeCD):
    #     for j in range(len(den)):
    #         NewCD[j][0] = den[i]
    for i in range(sizeCD):
        NewCD[j][0] = den[i]
        j = j + 1

    j = 0
    i = 0

    for i in range(sizeCD):
        for j in range(len(CD[0])):
            if CD[i][0] == j:
                CD[i][j+1] = 1

    j = 0
    i = 0

    #Crea el 1
    for j in range(3, len(CD[0])):
        CD[0][j] = CD[0][j-1] + 1

    #Crea el resto
    j = 0
    i = 0

    # while i !=
    #
    # # for i in range(1, sizeCD):
    # #     for j in range(1, len(CD[0])):
    # #         if CD[i][0] == j:
    # #             CD[i][j + 1] = 1
    # #         else:
    # #             CD[i][j] = CD[i - 1][j]
    #
    # USAR EL WHILE J != 1
    Currentcoin = []

    for i in range(len(den)):
        Currentcoin.append(den[i])

    combinations = [[0 for j in range(1,amount)] for i in range(coin)]

    for i in range(amount):
        for j in range(1,coin):
            combinations[i-1][j] = CD[i][j]




    print(combinations)


#User Input
den = [1,2,5,10,20]
camb = 14

array = CoinChose(den, camb)
print(array)

#JSON Operation
f = open("coin-change.json")

data = json.load(f)

print(data)

f.close()