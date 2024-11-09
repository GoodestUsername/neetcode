# Definition of Interval:
from collections import deque
from math import inf
from typing import List
import unittest


class Solution:
    def run(self, n: int) -> int:
        return n ^ 4294967296


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
        self.e(args=21, expected=2818572288)


if __name__ == "__main__":
    unittest.main()

# pop out each bit and put it in front
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         for i in range(32):
#             bit = (n >> i) & 1
#             res += bit << (31 - i)
#         return res


# optimal bit manip
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = n
#         res = (res >> 16) | (res << 16) & 0xFFFFFFFF
#         res = ((res & 0xFF00FF00) >> 8) | ((res & 0x00FF00FF) << 8)
#         res = ((res & 0xF0F0F0F0) >> 4) | ((res & 0x0F0F0F0F) << 4)
#         res = ((res & 0xCCCCCCCC) >> 2) | ((res & 0x33333333) << 2)
#         res = ((res & 0xAAAAAAAA) >> 1) | ((res & 0x55555555) << 1)
#         return res & 0xFFFFFFFF
