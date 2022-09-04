def two_sum(nums, target):
    visited = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in visited:
            return [visited[diff], i]
        else:
            visited[num] = i
