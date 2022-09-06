def max_profit(prices):
    low, high, profit = prices[0], prices[0], 0
    for i in range(1, len(prices)):
        if prices[i] < low:
            low, high = prices[i], prices[i]
        elif prices[i] > high:
            high = prices[i]
        profit = max(high - low, profit)
    return profit

# time:   O(n)
# memory: O(1)
