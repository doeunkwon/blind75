'''
You are given an array prices where prices[i] is the price of a given stock on
the ith day. You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that stock. Return
the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.
'''

def maxProfit(prices):
    l, r, maxProfit = 0, 1, 0
    while r < len(prices):
        currProfit = prices[r] - prices[l]
        maxProfit = max(maxProfit, currProfit)
        if prices[l] > prices[r]:
            l = r
        r += 1
    return maxProfit

# time:   O(n)
# memory: O(1)

# TEST
print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1])) # 0
