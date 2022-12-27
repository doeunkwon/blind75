'''
Suppose an array of length n sorted in ascending order is rotated between 1 and
n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]]. Given the sorted rotated
array nums of unique elements, return the minimum element of this array. You
must write an algorithm that runs in O(log n) time.
'''

def findMin(nums):
    l, r = 0, len(nums) - 1
    while (r - l) > 1:
        m = (r + l) // 2
        if nums[m] > nums[r]:
            l = m
        else:
            r = m
    return min(nums[l:r+1])

# time:   O(log n)
# memory: O(1)

print(findMin([3,4,5,1,2])) # 1
print(findMin([4,5,6,7,0,1,2])) # 0
print(findMin([11,13,15,17])) # 11
