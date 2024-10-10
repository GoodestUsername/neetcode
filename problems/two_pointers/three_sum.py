import enum
from typing import List
import unittest


class Solution:
    def run(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while r > l:
                sum = num + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif 0 > sum:
                    l += 1
                else:
                    sums.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and r > l:
                        l += 1
        return []


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

    def test_normal(self):
        self.e(args=[-1, 0, 1, 2, -1, -4], expected=[[-1, -1, 2], [-1, 0, 1]])

    def test_empty(self):
        self.e(args=[0, 1, 1], expected=[])

    def test_0s(self):
        self.e(args=[0, 0, 0], expected=[[0, 0, 0]])


if __name__ == "__main__":
    unittest.main()
