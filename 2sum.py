import time
# Two Sum problem


# "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."

# "You may assume that each input would have exactly one solution, and you may not use the same element twice."
#
# "You can return the answer in any order."


nums = [2, 7, 11, 15,23]
target = 38


def twosum(num, t)->list:
    num_map = {}
    for i in range(len(num)):
        remain = t - num[i]
        if remain in num_map:
            return [num_map[remain], i]
        num_map[nums[i]]=i
    return []

start = time.time()
print(twosum(nums,target))
print(time.time()-start)