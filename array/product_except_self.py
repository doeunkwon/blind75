def product_except_self(nums):
    res, right, left, r, l = [], [], [], 1, 1
    for num in nums:
        r *= num
        right.append(r)
    for num in nums[::-1]:
        l *= num
        left.append(l)
    left = left[::-1]
    for i in range(len(nums)):
        if i > 0:
            if i + 1 == len(nums):
                res.append(right[i-1])
            else:
                res.append(right[i-1] * left[i+1])
        else:
            res.append(left[i+1])
    return res

# time:   O(n)
# memory: O(n)
