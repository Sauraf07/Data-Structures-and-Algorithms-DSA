# Given an array nums and a target value target, return the indices of two numbers whose sum equals the target.
nums = [2,7,11,15]
target = 9

output = [0,1]

def two_sum(nums,target):
    seen = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i

    return []

print(two_sum(nums,target))