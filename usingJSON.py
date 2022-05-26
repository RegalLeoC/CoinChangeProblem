def usingJSON():

    import json

    with open("coin-change.json") as save:
        coinsave = json.load(save)
        save.close()


    five = coinsave

    # Lista de valores
    coinsname = []

    for i in five.keys():
        coinsname.append(int(i))

    #Lista de cantidades
    coinsamount = []

    for i in five.values():
        coinsamount.append(int(i))

    #Creacion de MasterList
    coinlist = []

    j = 0
    i = 0
    while j < len(coinsamount) and i < len(coinsname):
        coinlist.append([coinsname[i], coinsamount[j]])
        i = i + 1
        j = j + 1

    return (coinlist)

# print(usingJSON()[0])