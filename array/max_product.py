def max_product(nums):
    res, low, high = nums[0], 1, 1
    for num in nums:
        temp = low
        low = min(num, num*low, num*high)
        high = max(num, num*temp, num*high)
        res = max(res, high)
    return res

# time:   O(n)
# memory: O(1)
