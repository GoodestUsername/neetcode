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
