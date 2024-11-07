from collections import deque
import heapq
from typing import List
import unittest


# optimal solution by time complexity O(m * log k)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


# first attempt
# class Solution:
#     def run(self, stones: List[int]) -> int:
#         stones_arr = stones
#         stones_arr.sort()

#         while len(stones_arr) > 1:
#             s_heaviest = stones_arr.pop()
#             s_semi_heaviest = stones_arr.pop()
#             new_s = s_heaviest - s_semi_heaviest
#             if new_s > 0:
#                 stones_arr.append(new_s)
#                 stones_arr.sort()

#         if len(stones_arr):
#             return stones_arr[0]
#         return 0

# bucket sort optimal version, in this case because of the domain, 100 >= w >= 1
# Where n is the length of the stones array and w is the maximum value in the stones array.
# Time complexity: O(n+w)
# Space complexity: O(w)

# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:

#         maxStone = max(stones)
#         bucket = [0] * (maxStone + 1)
#         for stone in stones:
#             bucket[stone] += 1

#         first = second = maxStone
#         while first > 0:
#             if bucket[first] % 2 == 0:
#                 first -= 1
#                 continue

#             j = min(first - 1, second)
#             while j > 0 and bucket[j] == 0:
#                 j -= 1

#             if j == 0:
#                 return first
#             second = j
#             bucket[first] -= 1
#             bucket[second] -= 1
#             bucket[first - second] += 1
#             first = max(first - second, second)
#         return first


class Solution:
    def run(self, stones: List[int]) -> int:
        stones_arr = [-1 * stone for stone in stones]
        heapq.heapify(stones_arr)

        while len(stones_arr) > 1:
            s_heaviest = heapq.heappop(stones_arr)
            s_semi_heaviest = heapq.heappop(stones_arr)

            new_s = s_heaviest - s_semi_heaviest
            if 0 > new_s:
                heapq.heappush(stones_arr, new_s)
        if len(stones_arr):
            return abs(stones_arr[0])
        return 0


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    def test_avg(self):
        self.e(args=[2, 3, 6, 2, 4], expected=1)

    def test_min(self):
        self.e(args=[1, 2], expected=1)


if __name__ == "__main__":
    unittest.main()
