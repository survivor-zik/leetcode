# You are given an array of integers nums,
# there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
from collections import deque


def slidingwindowmax(nums: list, k: int) -> list:
    answer = []
    queue = deque()

    for i, n in enumerate(nums):
        while queue and queue[-1] < n:
            queue.pop()
        queue.append(n)
        if i >= k and nums[i - k] == queue[0]:
            queue.popleft()
        if i >= k - 1:
            answer.append(queue[0])
    return answer


print(slidingwindowmax([1, 3, -1, -3, 5, 3, 6, 7], 3))
