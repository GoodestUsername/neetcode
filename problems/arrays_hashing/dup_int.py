from typing import List
import unittest


class Solution:
    def run(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True

            numSet.add(num)
        return False


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    def tearDown(self):
        self.solution = None

    def test_dup(self):
        self.e(args=[1, 2, 3, 3], expected=True)

    def test_no_dup(self):
        self.e(args=[1, 2, 3, 4], expected=False)


if __name__ == "__main__":
    unittest.main()
