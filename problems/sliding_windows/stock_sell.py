from typing import List
import unittest


class Solution:
    def run(self, prices: List[int]) -> int:
        profit = 0

        lowest = prices[0]
        for price in prices:
            if lowest > price:
                lowest = price

            profit = max(profit, price - lowest)

        return profit


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

    def test_profit(self):
        self.e(args=[10, 1, 5, 6, 7, 1], expected=6)

    def test_no_profit(self):
        self.e(args=[10, 8, 7, 5, 2], expected=0)


if __name__ == "__main__":
    unittest.main()
