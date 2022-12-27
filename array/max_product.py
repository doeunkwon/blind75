'''
Given an integer array nums, find a subarray that has the largest product, and
return the product. The test cases are generated so that the answer will fit in
a 32-bit integer.
'''

def maxProduct(nums):
    res, low, high = nums[0], 1, 1
    for num in nums:
        temp = low
        low = min(num, num*temp, num*high)
        high = max(num, num*temp, num*high)
        res = max(res, high)
    return res

# time:   O(n)
# memory: O(1)

# TEST
print(maxProduct([2,3,-2,4])) # 6
print(maxProduct([-2,0,-1])) # 0
