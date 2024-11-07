from math import factorial
from typing import List
import unittest
import sys


sys.tracebacklimit = 0


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTreeCountLeaves(root) -> int:
    if root.val == 0:
        return 1
    if 0 > root.val:
        return 0

    root.left = TreeNode(root.val - 1)
    root.right = TreeNode(root.val - 2)

    return buildTreeCountLeaves(root.left) + buildTreeCountLeaves(root.right)


# tree solution, brute force?
# class Solution:
#     def run(self, n: int) -> int:
#         root = TreeNode(n, TreeNode(n - 1), TreeNode(n - 2))
#         return buildTreeCountLeaves(root)


class Solution:
    def run(self, n: int) -> int:
        ans = 2 if n % 2 == 0 else 1

        for k in range(1, ((n - 1) // 2) + 1):
            top = factorial(n - k)
            bot = factorial((n - 2 * k))
            if k != 1:
                bot *= factorial(k)
            ans += top / bot
        return int(ans)


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
        self.e(args=1, expected=1)

    def test_very_small(self):
        self.e(args=2, expected=2)

    def test_smaller(self):
        self.e(args=3, expected=3)

    def test_small(self):
        self.e(args=4, expected=5)

    def test_mid(self):
        self.e(args=5, expected=8)

    def test_big(self):
        self.e(args=7, expected=21)

    # 7
    # 1 1 1 1 1 1 1

    # 2 1 1 1 1 1
    # 1 2 1 1 1 1
    # 1 1 2 1 1 1

    # 1 1 1 2 1 1
    # 1 1 1 1 2 1
    # 1 1 1 1 1 2

    # 2 2 1 1 1
    # 2 1 2 1 1
    # 2 1 1 2 1
    # 2 1 1 1 2
    # 1 2 1 1 2
    # 1 1 2 1 2
    # 1 1 1 2 2

    # 2 2 2 1
    # 2 2 1 2

    # 2 1 2 2
    # 2 2 2 1

    # 6
    # 1 1 1 1 1 1

    # 2 1 1 1 1
    # 1 2 1 1 1
    # 1 1 2 1 1
    # 1 1 1 2 1
    # 1 1 1 1 2

    # 2 2 1 1
    # 2 1 2 1
    # 2 1 1 2
    # 1 2 1 2
    # 1 1 2 2

    # 2 2 2

    # 5
    # 1 1 1 1 1

    # 2 1 1 1
    # 1 2 1 1
    # 1 1 2 1
    # 1 1 1 2

    # 2 2 1
    # 2 1 2
    # 1 2 2

    # 4
    # 1 1 1 1

    # 2 1 1
    # 1 2 1
    # 1 1 2

    # 2 2

    # 3
    # 1 1 1

    # 2 1
    # 1 2

    # starts at 1 case
    # start with n amount of 1's
    # decrease 1 and replace with 2
    # there will be n - 1 choose x options, repeats for x times where x is n // 2
    # multiply result by 2 and subtract 1


if __name__ == "__main__":
    unittest.main()
