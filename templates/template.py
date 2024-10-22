from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, s: str, t: str) -> bool:
        return True


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(answer, expected)

    def test_dup(self):
        self.e(args=dict(s="jar", t="jam"), expected=True)


if __name__ == "__main__":
    unittest.main()
