# Definition of Interval:
from collections import deque
from math import inf
from typing import List
import unittest


# first attempt, O(n"2)
class Solution:
    def run(self, digits: List[int]) -> bool:
        carry = True

        for i in range(len(digits) - 1, -1, -1):
            num = digits[i]
            if carry:
                num += 1
            carry = num >= 10
            digits[i] = num % 10 if carry else num

        if carry:
            digits.insert(0, 1)
        return digits


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

    def test_non_carry_over(self):
        self.e(args=[1, 2, 3, 4], expected=[1, 2, 3, 5])

    def test_carry_over(self):
        self.e(args=[9, 9, 9], expected=[1, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()


# optimal, no need to check next number if current doesn't have a carry to effect
# the next, also digit will always be 0 if carry increases current to 10, so just keep
# going without a carry variable
#
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         n = len(digits)
#         for i in range(n - 1, -1, -1):
#             if digits[i] < 9:
#                 digits[i] += 1
#                 return digits
#             digits[i] = 0

#         return [1] + digits
