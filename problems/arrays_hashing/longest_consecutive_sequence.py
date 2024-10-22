from typing import List
import unittest
import sys

sys.tracebacklimit = 0

# non recursive version
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         num_set = set(nums)  # O(n) to create a set
#         longest_streak = 0

#         for num in num_set:
#             # Only start counting from the beginning of a sequence
#             if num - 1 not in num_set:
#                 current_num = num
#                 current_streak = 1

#                 # Count the length of the consecutive sequence
#                 while current_num + 1 in num_set:
#                     current_num += 1
#                     current_streak += 1

#                 longest_streak = max(longest_streak, current_streak)

#         return longest_streak


class Solution:
    def helper(self, target: int, numDict: dict[int, int]) -> int:
        if target not in numDict:
            return 0

        return 1 + self.helper(target + 1, numDict)

    def run(self, nums: List[int]) -> int:
        numDict = {}

        for i, num in enumerate(nums):
            numDict[num] = i

        max_len = 0
        for i, num in enumerate(nums):
            if num - 1 not in numDict:
                seq_len = self.helper(num, numDict)
                max_len = max(max_len, seq_len)
        return max_len


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    def test_ordered(self):
        # self.e(args=[2, 20, 4, 10, 3, 4, 5], expected=4)
        self.e(args=[2, 4, 3, 4, 5], expected=4)

    def test_unordered(self):
        self.e(args=[0, 3, 2, 5, 4, 6, 1, 1], expected=7)


if __name__ == "__main__":
    unittest.main()
