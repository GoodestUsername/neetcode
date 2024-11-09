# Definition of Interval:
from collections import deque
from math import inf
from typing import List
import unittest

# first attempt, no bit manipulation
# class Solution:
#     def run(self, nums: List[int]) -> int:
#         max_n = 0
#         sum_n = 0
#         contains_itself = (
#             False  # since the formula needs the max num, if max num is not
#         )
#         # the formula doesn't work, and the array is from 0 to len(nums) for the number
#         # range so it must be the len(nums)

#         for num in nums:
#             sum_n += num
#             max_n = max(max_n, num)
#             contains_itself = len(nums) == num or contains_itself

#         if not contains_itself:
#             return len(nums)

#         expected = (max_n * (max_n + 1)) / 2
#         return int(expected - sum_n)


# xor solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n
        for i in range(n):
            xor ^= i ^ nums[i]
        return xor


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

    def test_missing_0(self):
        # 01
        # 10
        # 11

        # 00
        self.e(args=[1, 2, 3], expected=0)

    def test_missing_1(self):
        # 00
        # 10

        # 01
        self.e(args=[0, 2], expected=1)

    def test_missing_arr_len_num(self):
        # 00
        # 01

        # 10
        self.e(args=[0, 1], expected=2)

    def test_missing_mid(self):
        # 00
        # 01
        # 11

        # 10
        self.e(args=[3, 0, 1], expected=2)


if __name__ == "__main__":
    unittest.main()
