from collections import defaultdict, deque
from math import ceil, floor, inf
from typing import List
import unittest
import sys

# sys.tracebacklimit = 0


class Solution:
    def run(self, nums: List[int]) -> int:
        nums_len = len(nums) - 1

        l = 0
        r = nums_len

        cur_min = nums[l]

        while r >= l:
            m = l + ((r - l) // 2)
            left = m - 1
            right = m + 1 if nums_len > m else 0
            if nums[left] > nums[m] and nums[right] > nums[m]:  # case 2
                return nums[m]
            if nums[m] > nums[left] and nums[m] > nums[right]:  # case 1
                return nums[right]
            if nums[m] > cur_min:
                cur_min = nums[m]
                l = m + 1
            else:
                r = m - 1

        return nums[m]


# rotated for first location searched to be the end point 4 5 [6] 1 2 3
# bigger than both sides
# problem solved

# rotated for first location searched to be the mid point 5 6 [1] 2 3 4
# smaller than both sides
# problem solved

# rotated for first location searched to be regular       6 1 [2] 3 4 5
# bigger than left, smaller than right

# rotated for first location searched to be reversed      3 4 [5] 6 1 2
# bigger than left, smaller than right

# if the second location is greater than the first location, then the pivot cannot be in
# that range

# [1, 2, 3]
# [3, 1, 2]
# [2, 3, 1]


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

    def test_min(self):
        self.e(
            args=[1],
            expected=1,
        )

    def test_rot_min_rot_0(self):
        self.e(
            args=[1, 2],
            expected=1,
        )

    def test_rot_min_rot_1(self):
        self.e(
            args=[2, 1],
            expected=1,
        )

    def test_rot_4(self):
        self.e(
            args=[3, 4, 5, 6, 1, 2],
            expected=1,
        )

    def test_rot_2(self):
        self.e(
            args=[4, 5, 0, 1, 2, 3],
            expected=0,
        )

    def test_rot_0(self):
        self.e(
            args=[4, 5, 6, 7],
            expected=4,
        )


if __name__ == "__main__":
    unittest.main()


# shorter syntax, pretty much same logic
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         start, end = 0, len(nums) - 1
#         curr_min = float("inf")

#         while start < end:
#             mid = start + (end - start) // 2
#             curr_min = min(curr_min, nums[mid])

#             # right has the min
#             if nums[mid] > nums[end]:
#                 start = mid + 1

#             # left has the  min
#             else:
#                 end = mid - 1

#         return min(curr_min, nums[start])
