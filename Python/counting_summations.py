def count_partitions(n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[0][i] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j]

    return dp[n][n] - 1


print(count_partitions(100))
