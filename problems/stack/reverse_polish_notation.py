from collections import deque
from math import floor
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        operands = deque()

        for token in tokens:
            if token in operators:
                operand_2 = operands.pop()
                operand_1 = operands.pop()
                operands.append(operators[token](operand_1, operand_2))
            else:
                operands.append(int(token))

        return operands[-1]


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
        self.e(args=["1", "2", "+", "3", "*", "4", "-"], expected=5)

    def test_multi_operator_chain(self):
        self.e(
            args=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
            # 10 6 9 3
            # 10 6 12
            # 10 6 12 -11
            # 10 6 12 * -11
            # 10 6 -132
            expected=22,
        )


if __name__ == "__main__":
    unittest.main()
