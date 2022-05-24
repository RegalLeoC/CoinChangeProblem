def CoinChange(coins, change):
    amountmon = len(coins)

    # Creacion de Tabla

    CD = [[0 for j in range(change + 1)] for i in range(amountmon)]


    for i in range(amountmon):
        for j in range(change+1):
            if j >= coins[i]:
                for k in range(i, amountmon):
                    CD[k][j] = CD[i][j - coins[i]] + 1


    smol = 0

    for i in range(amountmon):
        for j in range(change+1):


    print(CD)


# User Input

coins = 1, 2, 5, 10, 20
change = 14

tabla = CoinChange(coins, change)