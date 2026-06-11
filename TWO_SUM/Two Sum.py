nums = [1,2,3,4,6]
target = 6
left = 0
right = len(nums) - 1
while left < right:
    
    current_sum = nums[left] + nums[right]
    if current_sum == target:
        print([left, right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

