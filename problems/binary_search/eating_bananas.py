from collections import defaultdict, deque
from math import ceil, floor, inf
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + floor((r - l) / 2)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1


class Solution:
    def run(self, piles: List[int], h: int) -> int:
        min_hours = h // len(piles)
        # if min_hours == 1:
        #     return max(piles)

        k = max(piles) // min_hours

        # if (piles[i] // k) + len(piles) - 2 > h:
        #     k = min(k, )

        return k


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(answer, expected)

    def test_contains(self):
        self.e(
            args=dict(piles=[1, 4, 3, 2], h=9),
            expected=2,
        )

    def test_missing(self):
        self.e(
            args=dict(piles=[25, 10, 23, 4], h=4),
            expected=25,
        )


if __name__ == "__main__":
    unittest.main()

# optimal
# def run(self, nums: List[int], target: int) -> int:
#     l, r = 0, len(nums) - 1

#     while l <= r:
#         m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
#         if nums[m] > target:
#             r = m - 1
#         elif nums[m] < target:
#             l = m + 1
#         else:
#             return m
#     return -1
