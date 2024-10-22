from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def helper(self, n: int, cur_base: str, openings: int, closings: int) -> List[str]:
        if closings == n and openings == n:
            return [cur_base]

        iterations = []

        if n > openings:
            iterations.extend(self.helper(n, cur_base + "(", openings + 1, closings))

        if n > closings and openings > closings:
            iterations.extend(self.helper(n, cur_base + ")", openings, closings + 1))

        return iterations

    def run(self, n: int) -> List[str]:
        return self.helper(n, "(", 1, 0)


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

    def test_all(self):
        self.e(args=1, expected=["()"])

    def test_multi_operator_chain(self):
        self.e(
            args=3,
            expected=["((()))", "(()())", "(())()", "()(())", "()()()"],
        )


if __name__ == "__main__":
    unittest.main()

# stack solution
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = []
#         res = []

#         def backtrack(openN, closedN):
#             if openN == closedN == n:
#                 res.append("".join(stack))
#                 return

#             if openN < n:
#                 stack.append("(")
#                 backtrack(openN + 1, closedN)
#                 stack.pop()
#             if closedN < openN:
#                 stack.append(")")
#                 backtrack(openN, closedN + 1)
#                 stack.pop()

#         backtrack(0, 0)
#         return res
