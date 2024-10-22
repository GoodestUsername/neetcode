from collections import defaultdict, deque
from math import ceil, floor, inf
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        last_location = -1
        while True:
            cur_location = floor((r + l) / 2)

            if last_location == cur_location:
                break

            if nums[cur_location] == target:
                return cur_location

            if nums[cur_location] > target:
                r = cur_location
            else:
                l = cur_location

            last_location = cur_location

        return -1


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

    # def test_contains_3(self):
    #     self.e(
    #         args=dict(nums=[-1, 0, 2, 4, 6, 8], target=4),
    #         expected=3,
    #     )

    # def test_contains_9(self):
    #     self.e(
    #         args=dict(nums=[-1, 0, 3, 5, 9, 12], target=9),
    #         expected=4,
    # )

    def test_at_last(self):
        self.e(
            args=dict(nums=[-1, 0, 3, 5, 9, 12], target=12),
            expected=5,
        )

    # def test_missing(self):
    #     self.e(
    #         args=dict(nums=[-1, 0, 2, 4, 6, 8], target=3),
    #         expected=-1,
    #     )


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
