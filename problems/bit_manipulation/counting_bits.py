# Definition of Interval:
from collections import deque
from math import inf
from typing import List
import unittest


# first attempt
class Solution:
    def run(self, n: int) -> bool:
        sum = 0
        for i in range(32):
            sum += (n >> i) & 1
        return sum


# built in function
# class Solution:
#     def run(self, n: int) -> int:
#         return bin(n).count("1")


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

    def test_ls(self):
        self.e(args=11, expected=3)

    def test_min(self):
        self.e(args=23, expected=4)

    def test_avg(self):
        self.e(args=2147483645, expected=30)


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
