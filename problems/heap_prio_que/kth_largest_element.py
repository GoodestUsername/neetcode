from collections import deque
import heapq
from typing import List
import unittest

# first attempt
# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         nums.sort(reverse=True)

#         if len(nums) > k:
#             self.nums = nums[:k]
#         else:
#             self.nums = nums

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums.sort(reverse=True)

#         if len(self.nums) > self.k:
#             self.nums.pop()

#         return self.nums[self.k - 1]


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


class tests(unittest.TestCase):
    def test_dup(self):
        answer = []
        third_largest = KthLargest(3, [1, 2, 3, 3])
        answer.append(third_largest.add(3))
        answer.append(third_largest.add(5))
        answer.append(third_largest.add(6))
        answer.append(third_largest.add(7))
        answer.append(third_largest.add(8))

        self.assertEqual(answer, [3, 3, 3, 5, 6])


if __name__ == "__main__":
    unittest.main()
