from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, numbers: List[int], target: int) -> List[int]:
        indexSmaller = 0
        indexLarger = len(numbers) - 1

        while indexLarger > indexSmaller:
            if numbers[indexSmaller] + numbers[indexLarger] > target:
                indexLarger -= 1

            if target > numbers[indexSmaller] + numbers[indexLarger]:
                indexSmaller += 1

            if target == numbers[indexSmaller] + numbers[indexLarger]:
                return [indexSmaller + 1, indexLarger + 1]

        return [-1, -1]


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

    # def test_first(self):
    #     self.e(args=dict(numbers=[1, 2, 3, 4], target=3), expected=[1, 2])

    # def test_big(self):
    #     self.e(args=dict(numbers=[100, 200, 300, 500], target=500), expected=[2, 3])

    def test_neg(self):
        self.e(args=dict(numbers=[-10, -5, 0, 3, 7], target=-2), expected=[2, 4])


if __name__ == "__main__":
    unittest.main()
