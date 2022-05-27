import json
from usingJSON import *


def print_table(combinations):
    print(' ')
    print(' ')
    for i in range(len(combinations)):
        print(" ".join(map(str, combinations[i])))
    print(' ')


# def print_table(combinations):
#     for j in range(0, len(combinations)):
#         print('  '.join(combinations))

def DynamicCoins(array, camb, den, MasterList, amounts, save):
    bestans = [array[0][-1], 0, camb, 0]

    # while camb != 0:
    #     for i in range(len(array)):
    #         # for j in range(camb+1):
    #             if amounts[i] > 0:
    #                 if (camb - den[i]) >= 0:
    #                     if MasterList[i][camb+1] < bestans:
    #                         bestans = MasterList[i][camb+1]
    #

    while camb != 0:
        for i in range(len(array)):
            if amounts[i] > 0:
                if (camb - den[i]) >= 0:
                    if array[i][camb] < bestans[0]:
                        bestans = [array[i][camb], den[i], camb, i]
                        # print(bestans)
        camb = camb - bestans[1]
        amounts[bestans[-1]] = amounts[bestans[-1]] - 1
        save.append(bestans[1])
        bestans = [array[0][-1], 0, camb, 0]

    return save, amounts, den

def CoinChose(den, camb):
    # Create Dynamic Programming
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
                CD[i][j + 1] = 1

    # Crea el 1
    for j in range(3, len(CD[0])):
        CD[0][j] = CD[0][j - 1] + 1

    # Crea el resto

    combinations = [[0 for j in range(1, amount)] for i in range(coin)]
    monto = camb
    moneda = len(den)

    # Lo chido
    for i in range(len(CD)):
        for j in range(1, len(CD[0])):
            combinations[i][j - 1] = CD[i][j]

    for i in range(moneda):
        for j in range(monto + 1):
            if j >= den[i]:
                for k in range(i, moneda):
                    combinations[k][j] = combinations[i][j - den[i]] + 1

    # print(CD)
    # print(combinations)
    print_table(combinations)
    return combinations


# User Input
# JSON Operation
MasterList = usingJSON()
den = []
amounts = []
# Añade lista de denominaciones
for i in range(len(MasterList)):
    den.append(MasterList[i][0])

# Añade lista de cantidades de ese cambio
for i in range(len(MasterList)):
    amounts.append(MasterList[i][1])

# den = [1, 2, 5, 10, 20]

cost = int(input("Inserte el precio de su compra: "))

while cost > 0:
    print(f"Monto a pagar: {cost}")
    money = int(input("Inserte su dinero: "))
    cost = cost - money

if cost < 0:
    camb = -1 * (cost)
    print(f"Se le devolvera {camb} de cambio.")

if cost == 0:
    print("Cambio exacto.")

# camb = 14

# Creacion de arreglo
array = CoinChose(den, camb)
# print(array)
save = []

# Realizacion de Opreacion
end = (DynamicCoins(array, camb, den, MasterList, amounts, save))

print(end[0])



# JSON Operation
# print(usingJSON())

# f = open("coin-change.json")
# data = json.load(f)
# print(data)
# f.close()
