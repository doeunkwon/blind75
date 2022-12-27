'''
Given an integer array nums, find the subarray which has the largest sum and
return its sum.
'''

def maxSubArray(nums):
    maxSum, curSum = nums[0], 0
    for num in nums:
        curSum += num
        maxSum = max(maxSum, curSum)
        if curSum < 0:
            curSum = 0
    return maxSum

# time:   O(n)
# memory: O(1)

# TEST
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maxSubArray([1])) # 1
print(maxSubArray([5,4,-1,7,8])) # 23
