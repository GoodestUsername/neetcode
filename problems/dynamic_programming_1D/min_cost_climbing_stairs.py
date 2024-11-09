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


# could make with o(1) space by only using 3 slots at all time
# 1 2 3 4
# 1 2 3 4 = 10
# 2 4 = 6
class Solution:
    def run(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        past = dict()

        past[len(cost) - 1] = (len(cost) - 1, cost[-1])
        past[len(cost) - 2] = (len(cost) - 2, cost[-2])

        for i in range(len(cost) - 3, -1, -1):
            past[i] = min(
                (i, past[i + 1][1] + cost[i]),
                (i, past[i + 2][1] + cost[i]),
                key=lambda x: x[1],
            )

        return min(
            past[0][1],
            past[1][1],
        )


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

    # def test_min_multi_end(self):
    #     self.e(args=[99, 1], expected=1)

    # def test_min_multi_start(self):
    #     self.e(args=[1, 99], expected=1)
    def test_med(self):
        self.e(args=[1, 2, 3, 4, 5], expected=6)

    def test_small(self):
        self.e(args=[1, 2, 3], expected=2)

    def test_average(self):
        self.e(args=[1, 2, 1, 2, 1, 1, 1], expected=4)

    def test_skip_last(self):
        self.e(args=[0, 0, 0, 1], expected=0)

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


# optimal top down, DP
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 1

#         for i in range(n - 1):
#             temp = one
#             one = one + two
#             two = temp


#         return one
# optimal bottom up, DP
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         dp = [0] * (n + 1)
#         dp[1], dp[2] = 1, 2
#         for i in range(3, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
#         return dp[n]

# Space optimal DP
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 1

#         for i in range(n - 1):
#             temp = one
#             one = one + two
#             two = temp

#         return one
