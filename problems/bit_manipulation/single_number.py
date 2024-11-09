# Definition of Interval:
from collections import deque
from math import inf
from typing import List
import unittest


# non optimal solution
class Solution:
    def run(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] == nums[i + 1]:
                continue
            else:
                return nums[i]


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
        self.e(args=[3, 2, 3], expected=2)

    def test_avg(self):
        self.e(args=[7, 6, 6, 7, 8], expected=8)


if __name__ == "__main__":
    unittest.main()


# optimal, performs xor on each digit in binary.
# even numbers of 1's will cancel out, leaving the odd one remaining.
# ^ is xor not pow
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         res = 0
#         for num in nums:
#             res = num ^ res
#         return res
