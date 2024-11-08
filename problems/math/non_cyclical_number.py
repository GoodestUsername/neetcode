# Definition of Interval:
from math import inf
from typing import List
import unittest


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# first attempt, O(n"2)
class Solution:
    def run(self, n) -> bool:
        seen = dict()
        seen[n] = True
        while True:
            sum = 0
            while n != 0:
                sum += pow(n % 10, 2)
                n = n // 10

            if sum == 1:
                return True
            if sum in seen:
                return False

            seen[sum] = True
            n = sum
        return False


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

    # def test_non_cyclical(self):
    #     self.e(args=100, expected=True)

    # def test_cyclical(self):
    #     self.e(args=101, expected=False)

    def test_non_cyclical_min(self):
        self.e(args=1, expected=False)


if __name__ == "__main__":
    unittest.main()

# seems like it will repeat no later than log n times
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         slow, fast = n, self.sumOfSquares(n)

#         while slow != fast:
#             fast = self.sumOfSquares(fast)
#             fast = self.sumOfSquares(fast)
#             slow = self.sumOfSquares(slow)
#         return True if fast == 1 else False

#     def sumOfSquares(self, n: int) -> int:
#         output = 0

#         while n:
#             digit = n % 10
#             digit = digit**2
#             output += digit
#             n = n // 10
#         return output
