# Given an integer array nums and an integer k, return true
# if there are two distinct indices i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k.

n = [3, 2, 3, 1, 2, 3]
k = 4


def containsNearbyDuplicate(nums, k: int) -> bool:
    num_map = set()
    for i in range(len(nums)):
        if nums[i] in num_map:
            return True
        num_map.add(nums[i])
        if len(num_map) > k:
            num_map.remove(nums[i - k])
    return False


print(containsNearbyDuplicate(n, k))
