from math import floor

import unittest
import sys

sys.tracebacklimit = 0


class Solution:

    def run(self, s: str) -> bool:
        i = len(s) - 1
        for char in s:
            if not char.isalnum():
                continue

            while not s[i].isalnum() and i > 0:
                i -= 1

            if s[i].lower() != char.lower():
                return False

            i -= 1
        return True


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    def tearDown(self):
        self.solution = None

    def test_dup(self):
        self.e(args="Was it a car or a cat I saw?", expected=True)

    def test_no_dup(self):
        self.e(args="tab a cat", expected=False)


if __name__ == "__main__":
    unittest.main()
