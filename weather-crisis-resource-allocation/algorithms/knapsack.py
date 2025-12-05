def knapsack_allocate(regions, depot_capacity):
#Uses 0/1 knapsack to maximize urgency score.
    # Each region's 'value' = urgency
    # Each region's 'weight' = resources required
    n = len(regions)
    W = depot_capacity

    weights = [r.need for r in regions]
    values = [r.urgency for r in regions]

    # DP table
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    # Backtrack to find which items chosen
    chosen = []
    w = W

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:  # item included
            chosen.append(regions[i-1].name)
            w -= weights[i-1]

    # Build allocation result
    allocation = {r.name: (r.need if r.name in chosen else 0) for r in regions}

    return {
        "method": "knapsack_dp",
        "allocation": allocation,
        "total_value": dp[n][W],
        "remaining_capacity": W - sum(regions[i].need for i in range(n) if regions[i].name in chosen)
    }
