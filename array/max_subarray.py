def max_subarray(nums):
    curr, res = 0, nums[0]
    for num in nums:
        if curr <= 0:
            curr = 0
        curr += num
        res = max(res, curr)
    return res

# time:   O(n)
# memory: O(1)
