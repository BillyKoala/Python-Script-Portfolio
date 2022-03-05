"""
Billy Knight - March 2022

This module will define a target number
and will check a number list to find any
numbers which, when added to it, will
equal the target number.
"""

nums = [5,7,12,8,4,3]
target = 10
wanted = 0
found = ""
comma_count = len(nums)-1
output = "Target Sum: {} ".format(str(target)) + "["

try:
    for i in range(len(nums)):
        if nums[i] < target:
                wanted = target - nums[i]
                if nums[i] != wanted:
                    if wanted in nums:
                        found += str(nums[i]) + "+" + str(wanted) + "=" + str(target) + ""
                        found += ", " if comma_count > 0  else ""
        comma_count -= 1
    found += "]"
    
    print(output + found)

except Exception as e:
    print(e)

finally:
    pass
