# Definition of Interval:
from collections import deque
from math import inf
from typing import List
import unittest


# first attempt
# class Solution:
#     def run(self, n: int) -> bool:
#         output = []
#         for i in range(n + 1):
#             output.append(bin(i).count("1"))
#         return output
# 0 - 0 - 0
# 1 - 1 - 1
# 10 - 2 - 1
# 11 - 3 - 2

# 100 - 4 - 1
# 101 - 5 - 2
# 110 - 6 - 2
# 111 - 7 - 3

# 1000 - 8 - 1
# 1001 - 9 - 2
# 1010 - 10 - 2
# 1011 - 11 - 3

# 1100 - 12 - 2
# 1101 - 13 - 3
# 1110 - 14 - 3
# 1111 - 15 - 4

# 10000 - 16 - 1
# 10001 - 17 - 2
# 10010 - 18 - 2
# 10011 - 19 - 3

# 10100 - 20 - 2
# 10101 - 21 - 3
# 10110 - 22 - 3
# 10111 - 23 - 4

# 11000 - 24 - 2
# 11001 - 25 - 3
# 11010 - 26 - 3
# 11011 - 27 - 4


# [
# 0,
# 1,
# 1, 2,
# 1, 2, 2, 3,
# 1, 2, 2, 3, 2, 3, 3, 4
# 1,
# ]
class Solution:
    def run(self, n: int) -> bool:
        if 4 >= n:
            return [0, 1, 1, 2]

        output = [0] * (n + 1)
        pattern = [1, 2, 2, 3]

        b = 0
        prev = 0
        p = 0
        while n > b:
            # output[b] == 1
            p_i = 0
            for i in range(prev, b):
                output[i] = pattern[p_i] + p
                p_i += 1

                if p_i == 4:
                    p_i = 0
            prev = b + 1
            b = pow(2, p)
            p += 1

        return output


# actual way to repeat the pattern
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         dp = [0] * (n + 1)
#         for i in range(n + 1):
#             dp[i] = dp[i >> 1] + (i & 1)
#         return dp


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
        self.e(args=4, expected=[0, 1, 1, 2, 1])


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
