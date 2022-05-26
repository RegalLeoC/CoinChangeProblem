import math

def minCoingChange(coins, amount):
    minCoins = [[0 for j in range(amount)] for i in range(len(coins)+1)]
    minCoins[0] = 0
    for coin in coins:
        for i in range(amount):
            if((i-coin) >= 0):
                minCoins[i] = min(minCoins[i], (minCoins[i - coin] + 1))
    return minCoins

    print(minCoins)

# USer Input
coins = [1,2,5,10]
amount = 10
minCoingChange(coins, amount)