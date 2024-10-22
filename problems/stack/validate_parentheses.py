from collections import deque
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, s: str) -> bool:
        opening_parentheses_map = {"(": ")", "{": "}", "[": "]"}
        closing_parentheses_map = {")": "(", "}": "{", "]": "["}
        q = deque()

        for char in s:
            if char in opening_parentheses_map:
                q.append(opening_parentheses_map[char])
            elif len(q) > 0 and char == q[-1]:
                q.pop()
            elif char in closing_parentheses_map:
                return False

        return len(q) == 0


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

    def test_single_true(self):
        self.e(args="[]", expected=True)

    def test_multi_true(self):
        self.e(args="([{\}])", expected=True)

    def test_incorrect_order(self):
        self.e(args="[(])", expected=False)


if __name__ == "__main__":
    unittest.main()
