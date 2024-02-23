def countWays(coins, total):
    ways = [0] * (total + 1)
    ways[0] = 1  
    
    for coin in coins:
        for j in range(coin, total + 1):
            ways[j] += ways[j - coin]

    return ways[total]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200

print(countWays(coins, total))