def knapsack_optimize(values, capacity):
    n = len(values)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if values[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-values[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return {"max_value": dp[n][capacity]}
