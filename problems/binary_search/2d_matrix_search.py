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
    def run(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while r >= l:
            m = l + ((r - l) // 2)

            if target >= matrix[m][0] and matrix[m][-1] >= target:
                res = search(matrix[m], target)
                return res != -1
                # return True
            elif target > matrix[m][-1]:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1

        return False


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
            args=dict(
                matrix=[[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target=10
            ),
            expected=True,
        )

    def test_missing(self):
        self.e(
            args=dict(
                matrix=[[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target=15
            ),
            expected=False,
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
