'''
Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.
'''

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# time:   O(n)
# memory: O(n)

# TEST
print(contains_duplicate([1,2,3,1])) # True
print(contains_duplicate([1,2,3,4])) # False
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # True
